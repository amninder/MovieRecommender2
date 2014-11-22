from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from movie_names.models import *

movie_dict = {}

def readMovieNames(request):
	return HttpResponse("Hello World")