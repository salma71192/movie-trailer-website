""" Display different movies through Media Class."""

import fresh_tomatoes
import media

""" Finding Nemo movie (an instance of media class):
    movie title, story line, poster image, trailer."""
nemo = media.Media(
  "Finding Nemo",
  "A father fish and his friend cross the ocean to find his lost son",
  "http://img.moviepostershop.com/finding-nemo-movie-poster-2003-1010711355.jpg",  # NOQA
  "https://www.youtube.com/watch?v=3JNLwlcPBPI"
  )

""" Moana movie (an instance of media class):
    movie title, story line, poster image, trailer."""
moana = media.Media(
  "Moana",
  "A brave girl saves her village and the whole world.",
  "https://pbs.twimg.com/media/CygQfgwVIAERyhI.jpg:large",  # NOQA
  "https://www.youtube.com/watch?v=LKFuXETZUsI"
  )

""" Baby Boss movie (an instance of media class):
    movie title, story line, poster image, trailer."""
baby_boss = media.Media(
  "Baby Boss",
  "A baby who leads the world.",
  "http://www.tenterfieldcinema.com.au/wp-content/uploads/2017/01/The-Boss-Baby-poster.jpg",  # NOQA
  "https://www.youtube.com/watch?v=k397HRbTtWI"
  )


# Store movies in an object to be passed to media file
movies = [
  nemo,
  moana,
  baby_boss
  ]

# open website in browser through fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
