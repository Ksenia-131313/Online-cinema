# from django.urls import path

# from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'genres', views.GenreViewSet, basename='genre')
router.register(r'ratings', views.RatingViewSet, basename='rating')

# Основные фронтенд-маршруты оставляем
frontend_patterns = [
    path("", views.MoviesView.as_view(), name="home"),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("accounts/profile/", views.profile, name='profile'),
    path("accounts/edit_profile/", views.edit_profile, name='edit_profile'),
    path('account/<pk>/delete', views.ProfileDeleteView.as_view(), name='delete_profile'),
    path('movie/<pk>/delete', views.MovieDeleteView.as_view(), name='delete_movie'),
]

urlpatterns = [
    path('api/', include(router.urls)),  # DRF API для Swagger
    path('', include(frontend_patterns)),  # фронтенд-маршруты
]

# urlpatterns = [
#     path("", views.MoviesView.as_view()),
#     path("filter/", views.FilterMoviesView.as_view(), name='filter'),
#     #path('sort/<str:sort_value>', views.sort_movie, name='sort_movie'),
#     #path("sort/", views.SortirovkaMoviesView.as_view(), name='sort'),
#     # path("sorti/", views.SortiMoviesView.as_view(), name='sorti'),
#     path("search/", views.Search.as_view(), name='search'),
#     path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
#     path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
#     path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
#     path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
#     path("accounts/profile", views.profile, name='profile'),
#     path("accounts/edit_profile", views.edit_profile, name='edit_profile'),
#     path('account/<pk>/delete', views.ProfileDeleteView.as_view(), name='delete_profile'),
#     path('movie/<pk>/delete', views.MovieDeleteView.as_view(), name='delete_movie'),

# ]
