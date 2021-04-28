from django.shortcuts import render
from django.views.generic import ListView, DetailView
from mainapp.models import Post
from mainapp.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class PostList(ListView):
    """
    
    Display all post from model.Post and their cooments

    **Context**
    :model: `mainapp.models.Post`

    **Template**
    :template: `mainapp/post_list.html`
    
    """
    model = Post

    def get_queryset(self):
        
        #print(self.model.objects.all())
        print(self.model.objects.all()[0].count_likes())
        return self.model.objects.filter(is_active=True)


class PostDetail(DetailView):
    """
    
    Display post and comments where post_pk = pk

    **Context**
    :model: `mainapp.models.Post`

    **Template**
    :template: `mainapp/post_detail.html`
    
    """
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs['pk'], is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, pk):
        if request.method == "POST":
            form = CommentForm(data=request.POST)
            if form.is_valid():
                form.save()
        return HttpResponseRedirect(reverse("mainapp:post", kwargs={"pk":pk}))