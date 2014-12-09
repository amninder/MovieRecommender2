import datetime
from haystack import indexes
from movie_data.models import ImdbMovie
from movie_data.models import ImdbDirector



class ImdbMovieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return ImdbMovie

    def index_queryset(self, using=None):
        """ Using when entire idex of model is updated """
        return self.get_model().objects.all().order_by("-title")

# class ImdbDirectorIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#
#     def get_model(self):
#         return ImdbDirector
#
#     def index_queryset(self, using=None):
#         """ Using when entire idex of model is updated """
#         return self.get_model().objects.all().order_by("-name")
