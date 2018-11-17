#import webbrowser to open browser on run
import webbrowser

#define a class movie
class Movie():
    #constructor to initialise class movie with 4 instance variables for name, story, poster and trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #instance method of class Movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
