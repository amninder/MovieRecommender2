from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import Genre
from movie_data.models import Movie
from movie_data.models import Rating

import os
import sys
import re
import datetime



class Command(BaseCommand):
    help = "Read movies from 'movies.dat'"

    def handle(self, *args, **options):
        count = 0
        with open("./data/ratings.dat", "r") as f:
            for line in f:
                st = re.split("::", line)
                user_id = st[0]
                movie_id = st[1]
                rating = st[2]
                timestamp = st[3]
                movie = Movie.objects.get(movie_id=movie_id)
                ratings = Rating(user_id=int(user_id), rating=float(rating), movie_id=movie, timestamp=datetime.datetime.fromtimestamp(float(timestamp)))
                ratings.save()
                count += 1
                # print "{}:{}".format(count, movie.title.encode(sys.stdout.encoding, 'replace'))
                # print("{} rated {}\t \t {}".format(movie.title.encode("utf8"), datetime.datetime.fromtimestamp(float(timestamp)), rating))
                print("Count: {}".format(count))
