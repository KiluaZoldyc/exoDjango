# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^admin/', include(admin.site.urls)),
]
