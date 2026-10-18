from django import forms
from django.contrib import admin
from .models import PaySubs, Subscriptions
from ckeditor_uploader.widgets import CKEditorUploadingWidget



@admin.register(PaySubs)
class PaySubsAdmin(admin.ModelAdmin):
    """Покупка подписки"""
    list_display = ("id", "is_active", "profile", "valid_from", "valid_until")
    list_display_links = ("valid_from",)
    list_filter = ["subscriptions", "is_active", ]


class MovieSubsForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Subscriptions
        fields = '__all__'

@admin.register(Subscriptions)
class SubscriptionAdmin(admin.ModelAdmin):
    """Подписки"""
    list_display = ("id", "title", "price", "url")
    list_display_links = ("title",)
    form = MovieSubsForm
# Register your models here.
