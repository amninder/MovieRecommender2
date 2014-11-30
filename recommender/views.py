from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from movie_data.models import Genre


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
        # response = HttpResponse(request.POST.get("movie_name_input"))
        print "post called"
        response = HttpResponse("Got your request")
        return response

    def get(self, request):
        return HttpResponse("Get Page for Return Movie Name")
