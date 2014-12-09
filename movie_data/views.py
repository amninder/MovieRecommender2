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



def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))
    suggestions = [result.title for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse("sample sentence", content_type='application/json')

class Autocomplete(View):

    """
        search query
    """
    def __init__(self):
        self.greet = "this is a sample sentence"

    def get(self, request):
        var = request.GET.get("q")
        sqs = SearchQuerySet().autocomplete(content_suto="Sam")
        suggestions = [result.title for result in sqs]
        for s in suggestions:
            print s
        return HttpResponse(self.greet)
