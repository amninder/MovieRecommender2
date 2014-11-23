from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.genre

class Movie(models.Model):
    movie_id = models.PositiveIntegerField('MovieID')
    title = models.CharField('Title',max_length=200)
    year = models.CharField("Year", max_length=4)
    genres = models.ManyToManyField(Genre)
    def __unicode__(self):
        return self.movie_id
