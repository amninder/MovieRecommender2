from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):

    def __unicode__(self):
        return self.genre

    genre = models.CharField(max_length=100)

class Movie(models.Model):

    def __unicode__(self):
        return "{}: {}".format(self.movie_id, self.title.encode("utf8"))

    movie_id = models.PositiveIntegerField('MovieID')
    title    = models.CharField('Title',max_length=200)
    year     = models.CharField("Year", max_length=4)
    genres   = models.ManyToManyField(Genre)

class Rating(models.Model):

    def __unicode__(self):
        return self.movie_id

    user_id   = models.PositiveIntegerField('MovieID')
    rating    = models.FloatField(validators = [ MinValueValidator(0.0), MaxValueValidator(5.0)])
    movie_id  = models.ForeignKey(Movie)
    timestamp = models.DateTimeField()
