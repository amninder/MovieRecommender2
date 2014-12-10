from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from movie_data.views import FindSimilarMovies
from movie_data.forms import SearchForm
from haystack.views import SearchView

urlpatterns = patterns('haystack.views',
	# url(r'^$', FindSimilarMovies.as_view(), name='index'),
	url(r'^$', SearchView(form_class=SearchForm, results_per_page=20), name='haystack_search'),
)
