from datetime import datetime, date
from django.utils import dateformat
from django.shortcuts import redirect, render
from django.views.generic.base import View

from Sunshine import settings
from movies.models import Profile
from .models import Subscriptions, PaySubs
from django.views.generic import ListView, DetailView
from .forms import PaySubsForm
from django.http import HttpResponse
from django.shortcuts import render
from dateutil.relativedelta import relativedelta


def add_paysubs_view(request):
    if request.method == 'POST':
        form = PaySubsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = PaySubsForm()
    return render(request, 'base_sub.html', {'form': form})



class SubscriptionView(ListView):
    """Список subs"""
    model = Subscriptions
    queryset = Subscriptions.objects.all()
    context_object_name = 'subscriptions_list'

class SubscroptionDetailView(DetailView):
    """Полное описание subs"""
    model = Subscriptions
    slug_field = "url"
    template_name = 'subscription/subscriptions_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = PaySubs.objects.values_list('profile_id', flat=True)

        dating = datetime.now()
        context['time_now'] = dating.strftime('%Y-%m-%d')
        data_months = datetime.now() + relativedelta(months=+1)
        context['time_months'] = data_months.strftime('%Y-%m-%d')
        data_year = datetime.now() + relativedelta(months=+12)
        context['time_year'] = data_year.strftime('%Y-%m-%d')
        return context



#         subscriptions = Subscriptions.objects.get(id=subscriptions)
#         paysubs = PaySubs(
#             titlePaySubs = titlePaySubs,
#             profile=profile,
#             subscriptions=subscriptions,
#             valid_from=valid_from,
#             valid_until=valid_until,
#             is_active=is_active
#         )
#         paysubs.save()
#         return True
#     except Profile.DoesNotExist:
#         return False
#     except Exception as e:
#         print(f"Error: {e}")
#         return False
    



"""На странице subs_detail пользователь покупает подписку

def user_subscription(request):
    profile_subs = PaySubs.objects.all() 
    return render(request, 'movies/user_subs.html', {'profile_subs': profile_subs})

def paysubs_info(request):
    model_paysubs = PaySubs
    return render(request, 'movies/profile.html', {'model_paysubs':model_paysubs})

1. Если подписка у профиля есть подписка и она активна, выводить ее название и время завершения на странице профиля
    Если подписки нет или она не активна, выводить либо "ничего", либо "Нет подписки"."""

"""
# def paysubs_activ(request):
#     modelPay = PaySubs.profile()
#     if Profile.user in modelPay:
#         if (PaySubs.valid_from < PaySubs.subscriptions < PaySubs.valid_until):
#             # Вывести на странице профиля название подписки и дату её окончания
#             return render(request, 'movies/profile.html', {Subscriptions.title} and {PaySubs.valid_until})
#         else:
#             # вывести на странице профиля "Ваша подписка закончилась"
#             return render(request, 'movies/profile.html', HttpResponse("Ваша подписка закончилась"))
#     else:
#         return HttpResponse("Нет подписки")



@method_decorator(login_required, name='dispatch')
class ProfilePayPaySubsCreateView(View):
     Создание покупки(оформление подписки) для пользователей на подписки 
    model = Profile
    def is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    def post(self):
        profile = self.model.objects.get('id')
        if profile in PaySubs.profile:
            return f'{Subscriptions.title}, до: {PaySubs.valid_until}'
        else:
            return f'Оформить подписку'
ПРИМЕР:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class AddReview(View):
    Отзывы
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
    """
