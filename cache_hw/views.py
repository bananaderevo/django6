from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import DetailView, ListView

from .models import Author, Post


class PostListView(ListView):
    paginate_by = 100
    model = Post
    fields = ['text', 'author']
    template_name = 'cache_hw/list_post.html'
