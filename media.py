import webbrowser

class Movie():

    """Initialize the values of title, storyline, poster_image url and trailer video link to the variables of Movie"""
    def __init__(self,movie_title,movie_storyline,trailer_youtube, poster_image):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
    """The function that opens the webpage containing the trailer video"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
