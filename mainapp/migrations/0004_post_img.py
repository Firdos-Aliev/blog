# Generated by Django 3.2 on 2021-05-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='post_img', verbose_name='Картинка'),
        ),
    ]