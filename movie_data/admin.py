__author__ = 'narota'
from django.contrib import admin
from movie_data.models import Genre
from movie_data.models import Movie

def get_genres(GenereAdmin, request, queryset):
    print "Custom Action"
get_genres.short_description = "Load data from 'movies.dat'"

class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'genre',)
    list_filter  = ('genre',)
    actions      = [get_genres]
admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'movie_id', 'title',)
    # list_filter  = ('title',)
admin.site.register(Movie, MovieAdmin)
