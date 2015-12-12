"""Design a media center webpage.

This doc controls the layout, look, and interactivity of the webpage
that houses your entertainment center and favorite media.
"""

import webbrowser
import os
import re


"""CSS styles and JavaScript interactivity for the page."""
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog  {
            margin-top: 100px;
            width: 640px;
            height: 480px;
        }
        .modal-text {
            background: #e1e1ea;
            border-radius: 20px;
            text-align: center;
            font-family: Times;
            border: 2px solid black;
        }
       .modal-text h2 {
            text-decoration: underline;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        // and add the storyline "in a nutshell" above the trailer
        $(document).on('click', '.movie-tile', function (event) {
            var description = $(this).attr('data-storyline') + " View the trailer below or ";
            var title = $(this).attr('data-title');
            var link = '<a href="' + $(this).attr('data-IMDB') + '">get much more info at IMDB.com</a>.'
            document.getElementById('movieHeader').innerHTML = title + ': In A Nutshell';
            document.getElementById('movieStoryline').innerHTML = description + link;
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


"""HTML for the main page layout and title bar"""
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-text">
          <h2 id="movieHeader"></h2>
          <p id="movieStoryline"></p>
        </div>
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Trailers for Your Favorite Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


"""An HTML template for a single movie entry"""
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-storyline="{movie_storyline}" data-title="{movie_title}" data-IMDB="{IMDB_url}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    """Create the HTML content for each movie tile.

    Keyword arguments:
    movies -- a list of Movie objects from the module Media.

    Behavior:
    Extract all of the relevant information from a movie by
    looping through each movie object in the provided list of movies.
    
    Return the relevant information as an HTML formatted string.
    Returned string is intended to be inserted as HTML into a webpage to
    facilitate interactive viewing of data for each movie in the list of movies.
    
    """
    content = ''
    for movie in movies:

        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            IMDB_url=movie.IMDB_url
        )
    return content


def open_movies_page(movies):
    """Create the movies web page.

    Keyword arguments:
    movies -- a list of Movie objects from the module Media.

    First, create or overwrite the file containing all of the webpage information.
    
    Second, generate and insert the content for each movie tile into the main content
    portion of the page.
    
    Third, append the main content of the page to the head of the page and write the
    result to the file containing all of the webpage information.

    Fourth, open the file containing all of the webpage information
    in the browser (in a new tab, if possible).
    """
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
