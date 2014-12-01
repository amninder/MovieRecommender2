# -- coding: utf-8 --
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from movie_data.models import ImdbTag

import os
import sys
import re
import unicodedata

file_path = os.getcwd()+"/data/imdb/"

class Command(BaseCommand):
    help      = "Read genere from 'movies.dat'"

    def handle(self, *args, **options):
        with open(file_path+"tags.dat", "r") as f:
            count = 0
            for line in f:
                fields = line.split("\t")
                tag_id = fields[0]
                value = fields[1].decode('latin-1').encode('utf-8')
                print "tag ID: {}, Tag Value: {}".format(tag_id,  value)
                count += 1
                tags = ImdbTag(tag_id=tag_id, value=value)
                tags.save()
            print "total Directors: {}".format(count)
