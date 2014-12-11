from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator


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

    user_id   = models.PositiveIntegerField('User ID')
    rating    = models.FloatField(validators = [ MinValueValidator(0.0), MaxValueValidator(5.0)])
    movie_id  = models.ForeignKey(Movie)
    timestamp = models.DateTimeField()

class ImdbMovie(models.Model):
    def __unicode__(self):
        return self.imdb_id
    movie_id  = models.PositiveIntegerField('MovieID')
    title     = models.CharField("Imdb Title", max_length=300)
    imdb_id   = models.CharField('IMDB MovieID', max_length=50)
    image_url = models.CharField(max_length=300, validators=[URLValidator()], blank=True)
    # year      = models.CharField(max_length=10)

class ImdbDirector(models.Model):
    def __unicode__(self):
        return self.name
    movie_id    = models.ForeignKey(Movie)
    director_id = models.CharField("Director ID", max_length=200)
    name        = models.CharField("Director Name", max_length=200)

class ImdbActor(models.Model):
    def __unicode__(self):
        return self.name
    movie_id = models.ForeignKey(Movie)
    actor_id = models.CharField("Director ID", max_length=200)
    name     = models.CharField("Director Name", max_length=200)
    rating   = models.FloatField(validators = [ MinValueValidator(0.0)])

class ImdbTag(models.Model):
    def __unicode__(self):
        return self.value
    tag_id = models.CharField("Tag ID", max_length=200)
    value  = models.CharField("Tag Value", max_length=200)

class ImdbMovieTag(models.Model):
    def __unicode__(self):
        return self.tag_id
    movie_id = models.ForeignKey(Movie)
    tag_id = models.ForeignKey(ImdbTag)
    weight = models.CharField("Weight", max_length=20)
class ThisUser(models.Model):
    def __unicode__(self):
        pass
    user = models.OneToOneField(User)
    movie = models.ForeignKey(ImdbMovie)
