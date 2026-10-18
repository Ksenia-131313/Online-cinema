from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages.views import flatpage
from django.urls import path, include

#from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('about/', flatpage, {'url': '/about/'}, name='about'),
    path('contact/', include('contact.urls')),
    path('', include('movies.urls')),
    path('subscription/', include('subscription.urls')), 
    path('accounts/', include('allauth.urls')),    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 # path('i18n/', include('django.conf.urls.i18n')), 
# urlpatterns += i18n_patterns(
#     path('pages/', include('django.contrib.flatpages.urls')),
#     path('contact/', include('contact.urls')), 
#     path("", include("movies.urls")),
# )

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include, re_path

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# # Swagger schema
# schema_view = get_schema_view(
#     openapi.Info(
#         title="API Documentation",
#         default_version='v1',
#         description="Документация API Online Cinema",
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
#     path('pages/', include('django.contrib.flatpages.urls')),
#     path('contact/', include('contact.urls')),
#     path('subscription/', include('subscription.urls')),
#     path('accounts/', include('allauth.urls')),

#     # Swagger — ставим ДО всех маршрутов, чтобы не перехватывались slug
#     re_path(r'^swagger/?$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
#     re_path(r'^redoc/?$', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

#     # DRF API для моделей фильмов
#     path('api/', include('movies.urls')),  # movies.urls теперь содержит DRF router + фронтенд

#     # Фронтенд-маршруты остаются внутри movies.urls
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
