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
            for line in f.readlines():
                var = line.replace("\t", "::")
                var = var.replace("\r\n", "")
                # print var[:]
                var = var.split("::")
                tag_id = var[0]
                value = var[1]
                # value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
                print "{}: {}".format(var[0], var[1])
                tag = ImdbTag(tag_id=tag_id, value=value)
                tag.save()
            # for line in f:
            #     fields = line.split("\t")
            #     tag_id = fields[0]
            #     # tag_id = unicodedata.normalize('NFKD', unicode(fields[0])).encode('ascii','ignore')
            #     # value = unicodedata.normalize('NFKD', unicode(fields[1])).encode('ascii','ignore')
            #     value = fields[1]
            #     print "{}: {}".format(value.split(" "), value)
            #     # tag = ImdbTag(tag_id=tag_id, value=value)
            #     # tag.save()
