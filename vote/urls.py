from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rate$', views.participation_rate, name='participation_rate'),
]