from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)
    text = models.TextField(verbose_name='Текст')
    time = models.TimeField(verbose_name='Время добавления/обновления', auto_now=True, auto_now_add=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    is_active = models.BooleanField(verbose_name='Активный', default=True)


class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(verbose_name='Текст')
    time = models.TimeField(verbose_name='Время добавления/обновления', auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(verbose_name='Активный', default=True)