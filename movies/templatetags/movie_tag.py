from django import template
from movies.models import Category, Movie
#Для регистрации темплейт тегов
register = template.Library()
#Возвращение списка категорий
@register.simple_tag()
def get_categories():
    #Вывод всех категорий
    return Category.objects.all()
#Получение и группировка последних фильмов
@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies():
    movies = Movie.objects.order_by('-id')
    return {'last_movies': movies}

