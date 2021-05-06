from django.views.generic import FormView, RedirectView, CreateView, DetailView, UpdateView
from django.contrib.auth.views import get_user_model
from django.http import HttpResponseRedirect
from authapp.forms import LoginForm, RegistrationForm, UserProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User



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


class UsersProfile(DetailView):
    """
    Display user profile

    **Context**
    :model: `User`

    **Template**
    :template: `authapp/user_profile.html`
    """
    model = get_user_model()
    template_name = 'authapp/user_profile.html'


class UserProfile(UpdateView):
    """
    Provides users the ability to change profile
    """
    form_class = UserProfileForm
    model = get_user_model()
    template_name = 'authapp/profile.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user