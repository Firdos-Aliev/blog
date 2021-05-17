from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import get_user_model

class LoginForm(AuthenticationForm):
    """
    Form to login

    **Fields**
    :field: `username`
    :field: `password`
    """
    class Meta:
        model = get_user_model()
        fields = ("username", "password")

class RegistrationForm(UserCreationForm):
    """
    Form to registration

    **Fields**
    :field: `username`
    :field: `email`
    """
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class UserProfileForm(UserChangeForm):
    """
    Form to change profole

    **Fields**
    :field: `username`
    :field: `email`
    :field: `first_name`
    :field: `last_name`
    """
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        