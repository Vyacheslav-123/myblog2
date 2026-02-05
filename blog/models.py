from django.db import models
from django.contrib.auth.models import User
from django.template.context_processors import request
from django.utils import timezone
from django.utils.formats import date_format


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='Post-image',height_field=None, width_field=None, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    published_date = models.DateTimeField(default=timezone.now, verbose_name= 'Опубликовано')


    def __str__(self):
        return self.title