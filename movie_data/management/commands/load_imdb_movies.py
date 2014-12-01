from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import ImdbMovie
from movie_data.models import Movie

import os
import sys
import re

file_path = os.getcwd()+"/data/imdb/"

class Command(BaseCommand):
    help      = "Read genere from 'movies.dat'"

    def handle(self, *args, **options):
        with open(file_path+"movies.dat", "r") as f:
            for line in f:
                fields = line.split("\t")
                movie_id = fields[0]
                imdb_id = "tt{}".format(fields[2])
                image_url = fields[4]
                movie = Movie.objects.get(movie_id=movie_id)
                print "Movie ID: {}, Imdb ID: {}".format(movie_id, imdb_id)

                movie = ImdbMovie(title=movie, imdb_id=imdb_id, image_url=image_url)
                movie.save()
