# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import *
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('data-table/', data_table, name='data_table'),
    path('more-filters/', more_filters, name='more_filters'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
