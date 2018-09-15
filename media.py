import webbrowser  # this is a library used to open browser


class Video():  # this is the parent class
    """ This class provides a way to store information regarding the movie
        video"""

    def __init__(self, movie_title, duration):  # constructing pre-values
        self.title = movie_title  # title of the movie is sored
        self.movie_duration = duration  # duration of movie is stored


class Movie(Video):  # Movie class has some inherited properties of Video class
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # rating of the movies

    def __init__(self, movie_title, duration, movie_storyline, poster_image,
                 trailer):  # constructing pre-values
        Video.__init__(self, movie_title, duration)  # parent class is called
        self.storyline = movie_storyline  # movie story line is stored
        self.poster_image_url = poster_image  # URL of the image is stored
        self.trailer_youtube_url = trailer  # youtube URL is stored

    def show_trailer(self):  # show movie trailer function is defined
        # opens the tariler link in web browser
        webbrowser.open(self.trailer_youtube_url)
