from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^phone_number/(?P<phone_number>[0-9]+)$', views.phone_number, name='phone_number'),
]
