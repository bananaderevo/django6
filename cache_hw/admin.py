from django.contrib import admin

from .models import Author, Post, Quotes


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'info', 'post', 'quotes', 'id']


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'id']


@admin.register(Quotes)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ['quotes', 'author', 'id']
