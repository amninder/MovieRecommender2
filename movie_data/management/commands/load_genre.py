from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import Genre

import os
import sys
import re



class Command(BaseCommand):
    help = "Read genere from 'movies.dat'"

    def handle(self, *args, **options):
        with open("./data/movies.dat", "r") as f:
            for line in f:
                st = re.split("::", line)
                s = st[2][:-1].split("|")
                for name in s:
                    Genre.objects.get_or_create(genre=name)
