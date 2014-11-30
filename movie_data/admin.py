__author__ = 'narota'
from django.contrib import admin
from movie_data.models import Genre
from movie_data.models import Movie
from movie_data.models import Rating

def get_genres(GenereAdmin, request, queryset):
    print "Custom Action"
get_genres.short_description = "Load data from 'movies.dat'"

class GenreAdmin(admin.ModelAdmin):

    list_display = ('pk', 'genre',)
    list_filter  = ('genre',)
    actions      = [get_genres]
admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):

    list_display = ('pk', 'movie_id', 'title', 'year',)
    list_filter  = ('year',)
admin.site.register(Movie, MovieAdmin)

class RatingAdmin(admin.ModelAdmin):

    list_display = ('pk', 'movie_id', 'rating',)
    list_filter  = ('rating',)
admin.site.register(Rating, RatingAdmin)
