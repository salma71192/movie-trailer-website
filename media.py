import webbrowser
""" Define the media class which have the media information"""


class Media(object):

    def __init__(
        self,
        movie_title,
        storyline,
        poster_image,
        trailer_youtube
    ):
        """ The constructor function:
            returns movie_title, storyline, poster_image, trailer_youtube"""
        self.title = movie_title
        self.story = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ function to Open movie trailer in browser."""
        webbrowser.open(self.trailer_youtube_url)
