from django.shortcuts import render
from django.views.generic import TemplateView, View

from movie_data.models import Genre


class Index(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		return context

class FindSimilarMovies(TemplateView):
    template_name = "similar_movies.html"
    def get(self, request, *args, **kwargs):
		count = Genre.objects.all()
		return render(request, template_name,
			{
				'count': 'POST',
				'data': count
			})
