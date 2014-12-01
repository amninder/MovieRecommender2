from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import Movie

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
                m_id = fields[0]
                director_id = fields[1]
                name = fields[2]
                # movie = Movie.objects.get(movie_id=int(movie_id))
                print "MovieID: {}, Director ID: {}, Director Name: {}".format(m_id, director_id, name)
            print "total Directors: {}".format(count)
