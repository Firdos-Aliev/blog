import django.forms as forms
from mainapp.models import Comments, Post


class CommentForm(forms.ModelForm):
    """
    Form to add comment

    **Fields**
    :field: `user_id`
    :field: `post_id`
    :field: `text`
    """
    class Meta:
        model = Comments
        fields = ("user", "post", "text")


class PostForm(forms.ModelForm):
    """
    Form to add post

    **Fields**
    :field: `name`
    :field: `text`
    :field: `img`
    :field: `user`
    """
    class Meta:
        model = Post
        fields = ("name", "text", "img", "user")


class PostUpdateForm(forms.ModelForm):
    """
    Form to add post

    **Fields**
    :field: `name`
    :field: `text`
    :field: `img`
    """
    class Meta:
        model = Post
        fields = ("name", "text", "img", "is_active")
