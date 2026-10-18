from django import forms
from requests import request
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Reviews, Rating, RatingStar


from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from subscription.models import Subscriptions

class ProfileForm(UserChangeForm):
    """Форма профиля на обновление данных"""
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)
        widgets = {
            "username": forms.TextInput(attrs={"class":"progress-list" }),
            "email": forms.EmailInput(attrs={"class":"progress-list"}),
            "first_name": forms.TextInput(attrs={"class":"progress-list"}),
            "last_name": forms.TextInput(attrs={"class":"progress-list"}),
        }
        

class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    captcha = ReCaptchaField()
    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control border"}),
            "email": forms.EmailInput(attrs={"class":"form-control border"}),
            "text": forms.Textarea(attrs={"class":"form-control border"}),
        }
    

class RatingForm(forms.ModelForm):
    #ФОрма добавления рейтинга
    #В queryset получаем все созданные звезды, widget - внешний вид звезд
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(),  empty_label=None)
    class Meta:
        model = Rating
        fields = ("star", )
