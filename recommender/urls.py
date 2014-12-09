from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from recommender.views import Index, FindSimilarMovies, ReturnMovieName
from movie_data.views import autocomplete
from movie_data.views import Autocomplete

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view(), name='index'),
    url(r'^get_movie/$', ReturnMovieName.as_view(), name='return_movie_name'),
    url(r'movies/', include('movie_data.urls')),
    # url(r'^blog/', include('blog.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^autocomplete/', Autocomplete.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
