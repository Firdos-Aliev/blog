import django.forms as forms
from mainapp.models import Comments


class CommentForm(forms.ModelForm):
    """
    Form to add comment

    **Fields**
    :field: `username`
    :field: `password`
    """
    class Meta:
        model = Comments
        fields = ("user", "post", "text")