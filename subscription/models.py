
from django.db import models
from django.urls import reverse
from datetime import datetime
from dateutil.relativedelta import relativedelta
from movies.models import Profile

class Subscriptions(models.Model):
    title = models.CharField("Заголовок", max_length=100, )
    month = models.CharField("Подзаголовок", default='месяц', max_length=50,)
    price = models.PositiveIntegerField("Цена", default=0,)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('subscriptions_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
    
class PaySubs(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, default=None, verbose_name="Пользователь")
    subscriptions = models.ForeignKey(Subscriptions, verbose_name="Подписка", on_delete=models.CASCADE, null=True, default=None)
    is_active = models.BooleanField("Активность", default=True)
    valid_from = models.DateField("Начало подписки", default=datetime.today)
    valid_until = models.DateField("Окончание подписки", default = datetime.today() + relativedelta(months=+1))
    def __str__(self):
        return self.subscriptions
    def __str__(self):
        return f"{self.profile}"
    def __str__(self):
        return f"{self.subscriptions.title, self.is_active, self.profile }"



    class Meta:
        verbose_name = "Оформленные подписки"
        verbose_name_plural = "Оформленная подписка"    

# Create your models here.
