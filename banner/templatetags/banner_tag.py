from django import template
from banner.models import Banner

#Для регистрации темплейт тегов
register = template.Library()
#Возвращение списка категорий
# @register.simple_tag()
# def get_banner():
#     #Вывод всех категорий
#     return Banner.objects.all()
#Получение и группировка последних фильмов
@register.inclusion_tag('banners/tags/last_images.html')
def get_last_image():
    img = Banner.objects.order_by('-id')[:1]
    return {'last_images': img}

# # @register.inclusion_tag('movies/tags/last_movie.html')
# # def get_last_movies():
# #     movies = Movie.objects.order_by('id')[:3]
# #     return {'header': movies}
