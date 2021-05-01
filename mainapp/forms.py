import django.forms as forms
from mainapp.models import Comments, Post


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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("name", "text", "user")