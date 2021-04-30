from django.shortcuts import render
from django.views.generic import ListView, DetailView
from mainapp.models import Post, Likes
from mainapp.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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


@login_required
def like(request, pk):
    """
    Add functionals of likes
    """
    try:
        like = Likes()
        like.user = request.user
        like.post = Post.objects.filter(pk=pk).first()
        like.save()
    except Exception:
        print("Лайк уже есть")
    return HttpResponseRedirect(reverse("mainapp:post", kwargs={"pk":pk}))
