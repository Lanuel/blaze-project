from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'body', 'created']

class IconAdmin(admin.ModelAdmin):
    model = Icon
    list_display = ['title', 'image', id]


admin.site.register(Post, PostAdmin)
admin.site.register(Icon, IconAdmin)

