from django.shortcuts import render
from django.views.generic import TemplateView, View

from movie_data.models import Genre



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
