from django.db.models import Count
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.shortcuts import render

from .models import Author, Post, Quotes


@cache_page(60)
def quotes(request):
    object_list = Quotes.objects.all()
    paginator = Paginator(object_list, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count_posts = Quotes.objects.annotate(num_posts=Count('quotes')).count
    return render(request, 'cache_hw/list_quotes.html', {'page_obj': page_obj,
                                                         'count_posts': count_posts})


@cache_page(60 * 15)
def authors(request):
    object_list = Author.objects.all()
    paginator = Paginator(object_list, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count_authors = Author.objects.annotate(num_authors=Count('name')).count
    return render(request, 'cache_hw/list_author.html', {'page_obj': page_obj,
                                                         'count_authors': count_authors})


@cache_page(60 * 15)
def posts(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count_posts = Post.objects.annotate(num_posts=Count('text')).count
    return render(request, 'cache_hw/list_post.html', {'page_obj': page_obj,
                                                       'count_posts': count_posts})

