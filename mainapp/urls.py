from django.urls import path
from mainapp import views

app_name = "mainapp"

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetail.as_view(), name="post"),
    path("post/create/", views.PostCreate.as_view(), name="post_create"),
    path("post/update/<int:pk>/", views.PostUpadate.as_view(), name="post_update"),
    path("post/delete/<int:pk>/", views.PostDelete.as_view(), name="post_delete"),
    path("like_post/<int:pk>/", views.like, name="like_post"),
    
]