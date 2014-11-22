from django.db import models

class MovieTitle(models.Model):
    _id            	= models.CharField(max_length = 100)
    title           = models.CharField(max_length = 100)

def readMovieNames(lines):
	movie_dict = {}
	for line in lines:
		# print line
		x = line.split("::")
		# print "Id: %s, Name: %s"%(x[0], x[1])
		movie_dict[x[0]] = x[1]
	print movie_dict
	return movie_dict