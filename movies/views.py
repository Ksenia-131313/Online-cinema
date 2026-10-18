from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.base import View

from subscription.models import PaySubs, Subscriptions
from .models import Movie, Genre, Rating, Profile, Actor
from .forms import ProfileForm, ReviewForm, RatingForm
from django.db.models import Q
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from .serializers import MovieSerializer, GenreSerializer, RatingSerializer
from .models import Movie, Genre, Rating


class ProfileDeleteView(DeleteView):
    model = User
    success_url ="/"
    template_name = "movies/delete_user.html"

class MovieDeleteView(DeleteView):
    model = Movie
    success_url ="/"
    template_name = "movies/delete_movie.html"


def profile(request):
    users = request.user
    s = Profile.objects.get(user = users)
    subscribers= Profile.objects.values()
    subid = PaySubs.objects.values_list('profile_id', flat=True)
    return render(request, 'movies/profile.html', {'subscribers':subscribers, 's': s, 'subid': subid })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request,'movies/profile.html')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'movies/edit_profile.html', {'form': form})


#Класс для вывода всех жанров и годов
class GenreYear:
    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Movie.objects.filter(draft=False).values('year').distinct()



def sort_movies(queryset, request):
    sort = request.GET.get("order", "-id")

    if sort == "title":
        return queryset.order_by("title", "-id")

    if sort == "-title":
        return queryset.order_by("-title", "-id")

    if sort == "year":
        return queryset.order_by("year", "-id")

    if sort == "-year":
        return queryset.order_by("-year", "-id")

    return queryset.order_by("-id")



class MoviesView(GenreYear, ListView):
    """Список фильмов"""
    model = Movie
    paginate_by = 8

    def get_queryset(self):
        queryset = Movie.objects.filter(draft=False)
        return sort_movies(queryset, self.request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["banner_movies"] = Movie.objects.filter(
            draft=False
        ).order_by("-id")[:5]

        context["selected_genres"] = self.request.GET.getlist("genre")
        context["selected_years"] = self.request.GET.getlist("year")

        return context


class MovieDetailView(DetailView, GenreYear):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['form'] = ReviewForm()
        context['profiles'] = PaySubs.objects.values_list('profile_id', flat=True)
        return context



class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
    
class FilterMoviesView(GenreYear, ListView):
    """Фильтрация фильмов"""
    model = Movie
    paginate_by = 10

    def get_queryset(self):
        queryset = Movie.objects.filter(draft=False)

        years = self.request.GET.getlist("year")
        genres = self.request.GET.getlist("genre")

        if years:
            queryset = queryset.filter(year__in=years)

        if genres:
            queryset = queryset.filter(genres__id__in=genres)

        queryset = queryset.distinct()

        return sort_movies(queryset, self.request)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["banner_movies"] = Movie.objects.filter(
            draft=False
        ).order_by("-id")[:5]

        context["selected_years"] = self.request.GET.getlist("year")
        context["selected_genres"] = self.request.GET.getlist("genre")

        return context
    #def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["selected_years"] = self.request.GET.getlist("year")
        context["selected_genres"] = self.request.GET.getlist("genre")

        return context#


    
class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
        
class JsonFilterMoviesView(ListView):
    """Фильтр фильмов в json"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)

class Search(GenreYear, ListView):
    """Поиск фильмов"""
    model = Movie
    paginate_by = 8

    def get_queryset(self):
        queryset = Movie.objects.filter(draft=False)

        query = self.request.GET.get("q", "").strip()

        if query:
            queryset = queryset.filter(title__icontains=query)

        return sort_movies(queryset, self.request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banner_movies"] = Movie.objects.filter(
                    draft=False
                ).order_by("-id")[:5]
        context["q"] = self.request.GET.get("q", "")
        context["selected_genres"] = self.request.GET.getlist("genre")
        context["selected_years"] = self.request.GET.getlist("year")

        return context
    



# DRF ViewSets для Swagger / API
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
