from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from movie_names.models import *
from movie_names.views import readMovieNames

urlpatterns = patterns('',
    url(r'^store/$', readMovieNames),
)