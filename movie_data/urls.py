from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView, DetailView
from movie_data.views import FindSimilarMovies, MovieView

from movie_data.forms import SearchForm
from movie_data.models import ImdbMovie

from haystack.views import SearchView

urlpatterns = patterns('haystack.views',
	# url(r'^$', FindSimilarMovies.as_view(), name='index'),
	url(r'^$', SearchView(form_class=SearchForm, results_per_page=20), name='haystack_search'),
	# as convention DetailView takes 'model' as value passed
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model         = ImdbMovie,
        template_name = "sb-admin/imdb_movie.html"
    )),
	url(r'^movie/$', MovieView.as_view(), name="MovieView"),
)
