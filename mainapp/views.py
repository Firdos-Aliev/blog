from django.shortcuts import render
from django.views.generic import ListView
from mainapp.models import Post


class PostList(ListView):
    model = Post