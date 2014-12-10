from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from movie_data.models import Genre
from movie_data.models import Movie
from movie_data.models import ImdbMovie

import recsys.algorithm
from recsys.utils.svdlibc import SVDLIBC
from recsys.algorithm.factorize import SVD
recsys.algorithm.VERBOSE = True

import json
from django.utils import simplejson


class Index(TemplateView):
    def __init__(self):
        self.template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        return context

class FindSimilarMovies(TemplateView):
    def __init__(self):
        self.template_name = "similar_movies.html"
    def get(self, request, *args, **kwargs):
		count = Genre.objects.all()
		return render(request, template_name,
			{
				'count': 'POST',
				'data': count
			})

class ReturnMovieName(View):
    """docstring for ReturnMovieName"""
    def __init__(self):
        self.description = "Returns Movie Name"

    def post(self, request):
        movie_name = request.POST.get("movie_name_input")
        svd = SVD("data/movielens")
        data = svd.similar(int(movie_name))
        key = movie_name
        result = {}
        values = []
        for item in data:
            movie = Movie.objects.get(movie_id=item[0])
            values.append({"title":"{} ({})".format(movie.title, movie.year), "percent": format(item[1]*100, '.3f')})
        response = HttpResponse(json.dumps(values))
        return response

    def get(self, request):
        return HttpResponse("Get Page for Return Movie Name")

class ReturnSimilarMovies(View):

    def __init__(self):
        self.description = "return similar movies mapped to imdb_id"

    def post(self, request):
        data = simplejson.loads(request.body)
        print data
        imdb_id = request.POST.get("imdb_id")
        response = HttpResponse("imdb_id")
        return response

    def get(self, request):
        return HttpResponse("Not the page you are looking for.")


@csrf_exempt
def return_similar_movies(request):
    if request.method=="POST":
        data = json.loads(request.body)
        imdb_id = data["imdb_id"]
        print imdb_id
        similar_data = {}
        svd = SVD("data/movielens")
        movie_id = int(ImdbMovie.objects.get(imdb_id=imdb_id).movie_id)
        data = svd.similar(movie_id)
        total=[]
        for item in data:
            # movie = Movie.objects.get(movie_id=item[0])
            try:
                imdb = ImdbMovie.objects.get(movie_id=item[0])
                if imdb:
                    l = [imdb.imdb_id, imdb.movie_id, imdb.pk]
                    if l not in total:
                        total.append(l)
            except:
                continue
                print "{}: {}".format(movie.movie_id, imdb[0])
        for item in total[1:]:
            print "ImdbId: {}".format(item)
        print total
        response = HttpResponse(json.dumps(total))
        return response

    elif request.method=='GET':
        svd = SVD("data/movielens")
        # tt0240200
        movie_id = int(ImdbMovie.objects.get(imdb_id="tt0317705").movie_id)
        data = svd.similar(movie_id)
        total=[]
        for item in data:
            # movie = ImdbMovie.objects.get(movie_id=item[0])
            try:
                imdb = ImdbMovie.objects.get(movie_id=item[0])
                print "{}: {}".format(imdb.movie_id, imdb.imdb_id)
                if imdb:
                    l = [imdb.imdb_id, imdb.movie_id]
                    if l not in total:
                        total.append(l)
            except:
                print "exception thrown"
                continue
                print "{}: {}".format(movie.movie_id, imdb[0].imdb_id)
        print total

        return HttpResponse("Probably not the page you are looking for.")
