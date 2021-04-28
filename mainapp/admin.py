from django.contrib import admin
from mainapp.models import Post, Comments, Likes

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Likes)