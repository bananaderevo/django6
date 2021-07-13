from django.contrib import admin

from .models import Author, Post


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'info', 'post', 'id']


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'id']
