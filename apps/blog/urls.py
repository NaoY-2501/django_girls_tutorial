from django.conf.urls import include, url
from apps.blog import views

# http://127.0.0.1:8000/にアクセスすると,　views.post_listが動く
# name='post_list' はビューを特定するためのURLの名前
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
