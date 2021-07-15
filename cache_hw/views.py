from django.db.models import Avg, Count

from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import DetailView, ListView

from .models import Author, Post


class PostListView(ListView):
    paginate_by = 100
    model = Post
    fields = ['text', 'author']
    template_name = 'cache_hw/list_post.html'
    count = Post.objects.annotate(num_books=Count('text')).count


# def list(request):
#     object_list = Post.objects.all()
#     return render(request, 'cache_hw/list_post.html', {'object_list': object_list})