from django.conf.urls import include, url
from . import views

urlpattern = [
    url(r'^$', views.post_list, name='post_list'),
]