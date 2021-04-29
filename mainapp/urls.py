from django.urls import path
from mainapp import views

app_name = "mainapp"

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetail.as_view(), name="post"),
    path("like_post/<int:pk>/", views.like, name="like_post"),
]