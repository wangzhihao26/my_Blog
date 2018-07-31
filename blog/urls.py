from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
