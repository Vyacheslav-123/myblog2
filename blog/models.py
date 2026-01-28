from django.db import models
from django.contrib.auth.models import User
from django.template.context_processors import request
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(
                            )