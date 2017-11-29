from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^superuser', views.super_user, name='super_user'),
    url(r'^superuser/control', views.super_user_control, name='super_user_control'),
]