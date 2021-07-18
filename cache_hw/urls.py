from django.urls import include, path
from django.views.decorators.cache import cache_page


from . import views

app_name = 'cache_hw'
urlpatterns = [
    path('', views.posts, name='posts'),
    path('authors/', views.authors, name='authors'),
    path('quotes/', views.quotes, name='quotes'),

]
