from datetime import datetime,date

from django import forms

from .models import PaySubs

# from subscription.models import PaySubs

# class PayForm(forms.Form):
#     """Форма покупкu подписок"""
#     # titlePaySubs = forms.CharField()
#     profile = forms.IntegerField()
#     subscriptions = forms.IntegerField()
#     # is_active = forms.BooleanField(required=False)
#     valid_from = forms.DateTimeField()
#     valid_until = forms.DateTimeField()
#     # class Meta:
#     #     model = PaySubs
#     #     fields = ('profile', 'subscriptions', 'valid_from', 'valid_until',)
#     #     # widgets = {
#     #     #     "profile": forms.TextInput(attrs={"class":"progress-list"}),
#     #     #     "subscriptions": forms.EmailInput(attrs={"class":"progress-list"}),
#     #     #     "valid_from": forms.TextInput(attrs={"class":"progress-list"}),
#     #     #     "valid_until": forms.TextInput(attrs={"class":"progress-list"}),
#     #     # }



class PaySubsForm(forms.ModelForm):
    class Meta:

                model = PaySubs
                fields = ['profile', 'subscriptions', 'valid_from', 'valid_until']

                widgets = {
                    "profile": forms.TextInput(attrs={"class": "progress-list"}),
                    "subscriptions": forms.TextInput(attrs={"class": "progress-list"}),
                    "valid_from": forms.TextInput(attrs={"class": "progress-list"}),
                    "valid_until": forms.DateInput(attrs={"class": "progress-list"}),
                }