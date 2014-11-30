from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from movie_data.views import FindSimilarMovies

urlpatterns = patterns('',
	url(r'^$', FindSimilarMovies.as_view(), name='index'),
)
