from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import ImdbMovie
from movie_data.models import Movie

import os
import sys
import re
import urllib2

file_path = os.getcwd()+"/data/imdb/"
media_path = os.getcwd()+"/media/"

class Command(BaseCommand):
    help      = "Read genere from 'movies.dat'"

    def handle(self, *args, **options):
        total_movies = []
        count = 0
        with open(file_path+"movies.dat", "r") as f:
            for line in f:
                fields = line.split("\t")
                movie_id = fields[0]
                movie_title = fields[1].decode("latin-1").encode('utf-8')
                imdb_id = "tt{}".format(fields[2])
                image_url = fields[4]
                year = fields[5]
                if imdb_id not in total_movies:
                    total_movies.append(imdb_id)
                    if image_url !="":
                        if not os.path.isfile(media_path+"{}.jpg".format(imdb_id)):
                            print "{}.jpg <- {}".format(imdb_id, image_url)
                            image = urllib2.urlopen(image_url)
                            output = open("media/{}.jpg".format(imdb_id), "wb")
                            output.write(image.read())
                            output.close()
                        else:
                            print "{}.jpg Found in {}".format(imdb_id, media_path)
                    movie = Movie.objects.get(movie_id=movie_id)
                    print "title: {}, imdb_id: {}, image_url: {}".format(movie_title, imdb_id, image_url)
                    # imdb_movie = ImdbMovie(movie_id=movie, title=movie_title, imdb_id=imdb_id, image_url=image_url)
                    imdb_movie = ImdbMovie(movie_id=movie_id, title=movie_title, imdb_id=imdb_id, image_url=image_url)
                    imdb_movie.save()
                else:
                    print "{} already stored in database".format(imdb_id)
                    count += 1
        print "{} duplicate found.".format(count)
