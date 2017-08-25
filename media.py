import webbrowser

class Movie():
	'''
	This fuction creates a class called Movie, which has a set of atrabutes.
    These objects of the class are accsesed when this file is iported to another.
	'''


	VALID_RATINGS = ("g", "pg", "pd-13", "R")
	#the obejects of the fuc Movie
	def __init__(self, movie_title, movie_storyline, poster_image,
		trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	# show_traler opens trailer url when called
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

