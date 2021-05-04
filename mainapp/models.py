from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    """
    Stores a posts
    Related to:
        :model: `User`
    """
    name = models.CharField(verbose_name='Название', max_length=256)
    text = models.TextField(verbose_name='Текст')
    img = models.ImageField(verbose_name='Картинка', upload_to="post_img", blank=True)
    time = models.TimeField(verbose_name='Время добавления/обновления', auto_now=True, auto_now_add=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    is_active = models.BooleanField(verbose_name='Активный', default=True)

    def __str__(self):
        return self.name

    def count_likes(self):
        return len(self.likes_set.all())

class Comments(models.Model):
    """
    Stores a comments for posts
    Related to:
        :model: `User`
        :model: `Post`
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(verbose_name='Текст')
    time = models.TimeField(verbose_name='Время добавления/обновления', auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(verbose_name='Активный', default=True)

    def __str__(self):
        return self.text

class Likes(models.Model):
    """
    Stores a likes for posts
    Related to:
        :model: `User`
        :model: `Post`
    Double unique key:
        :field: `user`
        :field: `post`
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    
    class Meta:
        unique_together = ("user", "post")
