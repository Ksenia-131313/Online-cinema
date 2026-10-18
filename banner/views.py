from django.shortcuts import render
from django.views import View
from .models import Banner

class BannerViews(View):
    """Список баннеров"""
    def get(self, request):
        banners = Banner.objects.order_by('id')
        return render(request, 'include/header.html', {'banner_list':banners})



    # def get_image(self):
    #     return Banner.objects.last()
    # last_person = Banner.objects.last()
    # print(f"{last_person.image}")
