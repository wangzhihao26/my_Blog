from django.urls import path
from .import views
app_name = 'blog'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]