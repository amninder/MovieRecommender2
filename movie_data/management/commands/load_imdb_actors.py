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
        with open(file_path+"movie_actors.dat", "r") as f:
            count = 0
            for line in f:
                count+= 1
                fields = line.split("\t")
                movie_id = fields[0]
                actor_id = fields[1]
                actor_name = fields[2]
                rating = fields[3]
                print "MovieID: {}, Actor ID: {}, Actor Name: {}, Actor Rating: {}".format(movie_id, actor_id, actor_name, rating)
            print "total Actors: {}".format(count)
