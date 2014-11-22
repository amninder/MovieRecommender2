from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import Genre
from movie_data.models import Movie

import os
import sys
import re



class Command(BaseCommand):
    help = "Read movies from 'movies.dat'"

    def handle(self, *args, **options):
        with open("./data/movies.dat", "r") as f:
            for line in f:
                st = re.split("::", line)
                movie_id = st[0]
                movie_title = st[1]
                genres = st[2][:-1].split("|")
                # print "{}: {}: {}".format(movie_id, movie_title, genres)
                movie = Movie(movie_id=movie_id, title=movie_title)
                movie.save()
                for genre in genres:
                    movie.genres.add(Genre.objects.get(genre=genre).pk)
