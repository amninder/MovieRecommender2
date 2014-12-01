from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import Movie
from movie_data.models import ImdbDirector

import os
import sys
import re

file_path = os.getcwd()+"/data/imdb/"

class Command(BaseCommand):
    help      = "Read genere from 'movies.dat'"

    def handle(self, *args, **options):
        with open(file_path+"movie_directors.dat", "r") as f:
            count = 0
            for line in f:
                count+= 1
                fields = line.split("\t")
                movie_id = fields[0]
                director_id = fields[1]
                name = fields[2].decode('latin-1').encode('utf-8')
                movie = Movie.objects.get(movie_id=int(movie_id))
                print "Movie ID: {}, Director ID: {}, Director Name: {}".format(movie_id, director_id, name)

                imdb_director = ImdbDirector(movie_id=movie, director_id=director_id, name=name)
                imdb_director.save()
            print "total Directors: {}".format(count)
