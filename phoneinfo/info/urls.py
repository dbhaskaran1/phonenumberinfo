from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^current/date$', views.get_date, name='get_date'),
    url(r'^current/time$', views.get_time, name='get_time'),
    url(r'^phone_number/(?P<phone_number>[\w]+)$', views.phone_number, name='phone_number'),
    url(r'^phone_number/(?P<phone_number>[\w]+)/(?P<country_code>[\w]+)$', views.phone_number, name='phone_number'),
]
