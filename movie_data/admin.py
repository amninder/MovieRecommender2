__author__ = 'narota'
from django.contrib import admin
from movie_data.models import Genre
from movie_data.models import Movie
from movie_data.models import Rating
from movie_data.models import ImdbMovie
from movie_data.models import ImdbDirector
from movie_data.models import ImdbActor
from movie_data.models import ImdbTag
from movie_data.models import ImdbMovieTag
from movie_data.models import Note

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


class ImdbMovieAdmin(admin.ModelAdmin):
    list_display = ("title", "imdb_id", "image_url")
admin.site.register(ImdbMovie, ImdbMovieAdmin)

class ImdbDirectorAdmin(admin.ModelAdmin):
    list_display = ("director_id", "name")
admin.site.register(ImdbDirector, ImdbDirectorAdmin)

class ImdbActorAdmin(admin.ModelAdmin):
    list_display = ("actor_id", "name", "rating")
admin.site.register(ImdbActor, ImdbActorAdmin)

class ImdbTagAdmin(admin.ModelAdmin):
    list_display = ("tag_id", "value")
admin.site.register(ImdbTag, ImdbTagAdmin)

class ImdbMovieTagAdmin(admin.ModelAdmin):
    list_display = ("tag_id", "weight")
admin.site.register(ImdbMovieTag, ImdbMovieTagAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ("user", "pub_date", "title", "body")
admin.site.register(Note, NoteAdmin)
