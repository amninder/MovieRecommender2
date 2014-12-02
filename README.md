#Movie Recommender
## Get data files from
[MovieLens Imdb Daaset](http://files.grouplens.org/datasets/hetrec2011/hetrec2011-movielens-2k-v2.zip)

##Run following commands
This is Django based project to recommend movie based upon user rating. After sycing your database for first time do the following:

0. SyncDb
```
./manage.py syncdb
```

1. Generate Genre database by
```
./manage.py load_genre
```

2. Generate Movie Database by
```
./manage.py load_movie
```

3. Load Imdb Movies
```
./manage.py load_imdb_movies
```

4. Load Imdb Directors
```
./manage.py load_imdb_directors
```
5. Load Imdb Tags
```
./manage.py load_imdb_tags
```
6. Load Imdb Movie Tags
```
./manage.py load_imdb_movie_tags
```
