"""Define different types of media.

Currently, the only media defined is "movie."  However,
media could also include, for example, music or books.
"""

class Movie():
    """A representation of a movie.

    The object is a container for information related to a specific movie.
    """    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, IMDB_url):
        """Initialize a Movie object.

        Keyword arguments:
        movie_title -- the title of the movie
        movie_storyline -- a short description of the movie's plot
        poster_image -- a url to a poster image of the movie
        trailer_youtube -- a url to a YouTube trailer for the movie
        IMDB_url -- a url to the IMDB entry for the movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.IMDB_url = IMDB_url
