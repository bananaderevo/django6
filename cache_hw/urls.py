from django.urls import path

from . import views

app_name = 'cache_hw'
urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    ]