from django.urls import path, re_path
<<<<<<< HEAD
from . import views


=======
from .import views
>>>>>>> 86001fc87a2ed11c41a311988000a3a7f95a8531
app_name = 'blog'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 86001fc87a2ed11c41a311988000a3a7f95a8531
