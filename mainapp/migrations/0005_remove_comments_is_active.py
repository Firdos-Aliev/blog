# Generated by Django 3.2 on 2021-05-09 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='is_active',
        ),
    ]