from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    #Форма подписи по емаил#
    #placeholder - подсказка в поле ввода
    class Meta:
        model = Contact
        fields = ('email', )
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'ivanov.ivan@gmail.com'})
        }
        labels = {
            'email': ''
        }