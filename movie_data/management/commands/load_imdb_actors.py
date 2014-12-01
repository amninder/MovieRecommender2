from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import ImdbActor
from movie_data.models import Movie

import os
import sys
import re
import unicodedata

file_path = os.getcwd()+"/data/imdb/"

class Command(BaseCommand):
    help      = "Read from 'movie_actors.dat'"

    def handle(self, *args, **options):
        with open(file_path+"movie_actors.dat", "r") as f:
            count = 0
            for line in f:
                count+= 1
                fields = line.split("\t")
                movie_id = fields[0]
                actor_id = fields[1]
                name = fields[2].decode('latin-1').encode('utf-8')
                # name = fields[2].decode('latin-1')
                rating = fields[3]
                print "Name: {}, Rank: {}".format(name, rating)
                movie = Movie.objects.get(movie_id=int(movie_id))

                actor = ImdbActor(movie_id=movie, actor_id=actor_id, name=name, rating=rating)
                actor.save()
            print "total Directors: {}".format(count)
