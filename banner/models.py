from django.db import models


class Banner (models.Model):
    image = models.ImageField("Баннер", upload_to="banner/")
    url = models.SlugField(max_length=160, unique=True)
    
    def __str__(self):
        return self.url
    # def get_image(self):
    #     last_person = Banner.objects.order_by('-id')[:1]
    #     return(last_person)

 
    class Meta:
        verbose_name = "Центральный баннер"
        verbose_name_plural = "Список баннеров"
    

