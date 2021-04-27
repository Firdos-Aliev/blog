from django.shortcuts import render
from django.views.generic import ListView
from mainapp.models import Post


class PostList(ListView):
    """
    
    Display all post from model.Post and their cooments

    **Context**
    :model: `mainapp.models.Post`

    **Template**
    :template: `mainapp/post_list.html`
    
    """
    model = Post