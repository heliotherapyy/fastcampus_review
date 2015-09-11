from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'miniblog.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'miniblog.views.detail', name='detail'),
]
