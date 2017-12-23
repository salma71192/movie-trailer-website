""" Define the media class which have the media information"""

class Media(object):
	def __init__(self, movieTitle, storyLine, posterImage, trailerYoutube):
		self.title = movieTitle
		self.story = storyLine
		self.poster_image_url = posterImage
		self.trailer_youtube_url = trailerYoutube

	def show_trailer(self):
		""" Open movie trailer in browser. """
		webbrowser.open(self.trailer_youtube_url)
