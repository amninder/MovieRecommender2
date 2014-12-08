import datetime
from haystack import indexes
from movie_data.models import Note
from movie_data.models import ImdbMovie




class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    """docstring for ImdbMovieIndex"""
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Using when entire index of model is updated"""
        return self.get_model().objects.filter(pub_date__lte = datetime.datetime.now())

class ImdbMovieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return ImdbMovie

    def index_queryset(self, using=None):
        """ Using when entire idex of model is updated """
        return self.get_model().objects.all().order_by("-title")
