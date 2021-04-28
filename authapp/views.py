from django.views.generic import FormView, RedirectView, CreateView
from django.contrib.auth.views import get_user_model
from django.http import HttpResponseRedirect
from authapp.forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout


class UserLogin(FormView):
    """
    Provides users the ability to login
    """
    form_class = LoginForm
    template_name = 'authapp/login.html'
    success_url = '/'

    def form_valid(self, form):
        if form.get_user().is_active:
            login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


class UserLogout(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(UserLogout, self).get(request, *args, **kwargs)


class UserRegistration(CreateView):
    """
    Provides users the ability to registration
    """
    form_class = RegistrationForm
    template_name = 'authapp/registration.html'
    success_url = '/'
    #TO DO: перегрузить form_valid и сохранить пользователя вместе с профилем