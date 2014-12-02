from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import ImdbMovie

import os
import sys
import urllib2
import json

omdbapi_url = "http://www.omdbapi.com/?i={}&plot=short&r=json"

class Command(BaseCommand):
    help      = "Read genere from 'movies.dat'"

    def handle(self, *args, **options):
        movies = ImdbMovie.objects.all()
        count = 0
        miss = 0
        ids = []
        for item in movies:
            request = urllib2.Request(omdbapi_url.format(item.imdb_id))
            response = urllib2.urlopen(request)
            data = response.read()
            value = json.loads(data)
            if "Poster" in value.keys() and value["Poster"] != "N/A":
                movie = ImdbMovie.objects.get(imdb_id=item.imdb_id)
                movie.image_url = value["Poster"]
                movie.save()
                print "MovieID: {}\tPoster URL: {}".format(item.imdb_id, value["Poster"])
            else:
                count += 1
        print "total missing imdb_id: {}".format(count)
        # print "Total Misses: {}".format(miss)
