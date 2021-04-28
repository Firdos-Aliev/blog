from django.urls import path
from authapp import views

app_name = "authapp"

urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path("registration/", views.UserRegistration.as_view(), name="registration"),
]