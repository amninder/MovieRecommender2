
from recsys.algorithm.factorize import SVD
from recsys.utils.svdlibc import SVDLIBC
from recsys.datamodel.data import Data

import recsys.algorithm
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import Genre
from movie_data.models import Movie

import os
import sys
import re



class Command(BaseCommand):
    help = "testing for similarity"

    def handle(self, *args, **options):
        svd2 = SVD(filename='./data/movielens') # Loading already computed SVD model
        # Get two movies, and compute its similarity:
        ITEMID1 = 2    # Toy Story (1995)
        ITEMID2 = 2335 # A bug's life (1998)
        print "{}: {}".format(ITEMID1, svd2.similar(ITEMID1))
