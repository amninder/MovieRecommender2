from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse

from haystack.query import SearchQuerySet

from movie_data.models import Genre

import json



class FindSimilarMovies(TemplateView):
    def __init__(self):
        self.template_name = "sb-admin/similar_movies.html"

    def get_context_data(self, **kwargs):
        count = Genre.objects.all()
        context = super(Index, self).get_context_data(**kwargs)
        context["count"]  = count
        return context

    def get(self, request, *args, **kwargs):
        count = Genre.objects.all()
        return render(request, self.template_name,
            {
                'count': 'POST',
                'data': count
            })



class MovieView(View):

    def post(self, request, *args, **kwargs):
        print request.POST.get('pk-hidden')
        return HttpResponse("request.POST.get('pk-hidden')")

    def get(self, request, *args, **kwargs):
        return HttpResponse("get page")
