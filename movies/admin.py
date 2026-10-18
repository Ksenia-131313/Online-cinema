from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
#from modeltranslation.admin import TranslationAdmin

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


from ckeditor_uploader.widgets import CKEditorUploadingWidget




class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_film = forms.CharField(label='Фильм', widget=CKEditorUploadingWidget())
    description_trel = forms.CharField(label='Трейлер', widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"








@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name", "year", "country")
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ['publish', 'unpublish']
    form = MovieAdminForm 
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": (("poster", "get_image"),"banner", "description", 'description_film', 'description_trel')
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        # (None, {
        #     "fields": (("budget", "fees_in_usa", "fess_in_world"),)
        # }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')
#=================================================================================================
    #Создание "действий" на админке (опубликовать/снять с публикации)
    def unpublish(self, request, queryset):
        #Снять с публикации
        row_update = queryset.update(draft = True)
        if row_update == 1:
            massage_bit = "1 запись была обновлена"
        else:
            massage_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{massage_bit}')

    def publish(self, request, queryset):
        #Опубликовать
        row_update = queryset.update(draft = False)
        if row_update == 1:
            massage_bit = "1 запись была опубликована"
        else:
            massage_bit = f'{row_update} записей были опубликованы'
        self.message_user(request, f'{massage_bit}')


    publish.short_description = 'Опубликовать'
    publish.allowed_permission = ('change, ')#Чтобы изменять у пользователя должны быть права

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permission = ('change, ')

    get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "movie",  "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)


admin.site.site_title = "Администрирование Sunshine"
admin.site.site_header = "Администрирование Sunshine"

