from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    re_path(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]

