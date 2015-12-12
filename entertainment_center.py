"""Create a webpage that houses your favorite media.

Currently, the only objects that can be added to the entertainment center
are movies.
After creating the movies, the entertainment center produces the webpage.
"""

import media
import fresh_tomatoes


matrix = media.Movie("The Matrix",
                     "A group of free humans battle machine overlords in a struggle"
                     " to free the rest of the human race from virtual bondage.",
                     "http://2.bp.blogspot.com/-2F8gEE3lENI/UEFvWy-MCLI/AAAAAAAAMkA/P5O9gKXKLbs/s1600/The+Matrix+(1999)+1.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                     "http://www.imdb.com/title/tt0133093/")
rush_hour = media.Movie("Rush Hour",
                        "East meets West in this racial, buddy-cop comedy.",
                        "http://static.cinemagia.ro/img/db/movie/00/01/89/rush-hour-798893l.jpg",
                        "https://www.youtube.com/watch?v=rs_6Psn1XK0",
                        "http://www.imdb.com/title/tt0120812/?ref_=fn_al_tt_1")
fellowship_of_the_ring = media.Movie("The Fellowship of the Ring",
                                     "An enthralling adaptation of J.R.R. Tolkien's classic fantasy novel.",
                                     "http://1.bp.blogspot.com/-huikg011hHE/UD3GffyCI8I/AAAAAAAAL8c/2lqUtOVUJok/s1600/The+Fellowship+Of+The+Ring+(2001)+1.jpg",
                                     "https://www.youtube.com/watch?v=V75dMMIW2B4",
                                     "http://www.imdb.com/title/tt0120737/?ref_=nv_sr_1")
usual_suspects = media.Movie("The Usual Suspects",
                             "A crime thriller with one of the greatest plot twists in cinema history.",
                             "http://www.dvdsreleasedates.com/posters/800/T/The-Usual-Suspects-movie-poster.jpg",
                             "https://www.youtube.com/watch?v=oiXdPolca5w",
                             "http://www.imdb.com/title/tt0114814/?ref_=nv_sr_1")
anchorman = media.Movie("Anchorman",
                        "Will Ferrell as a TV news anchorman in the 1970s, supported by Paul Rudd and Steve Carrell.  Enough Said.",
                        "http://www.publispain.com/posters/anchorman.jpg",
                        "https://www.youtube.com/watch?v=-T3wnP91OnI",
                        "http://www.imdb.com/title/tt0357413/?ref_=nv_sr_2")
a_new_hope = media.Movie("Star Wars",
                         "A futuristic struggle between an evil galactic empire and a band of freedom-fighting rebels.",
                         "http://www.rock.com/assets/products/349879/large/star-wars-a-new-hope-poster-13828.jpg",
                         "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                         "http://www.imdb.com/title/tt0076759/?ref_=nv_sr_2")
judgement_day = media.Movie("Terminator 2",
                            "A cyborg from the future protects the future leader of mankind from another cyborg.",
                            "http://2.bp.blogspot.com/-WpDGHJpyjfQ/UEkDASTeLeI/AAAAAAAANrc/pXEv7w86ckc/s1600/Terminator+2+(1991)+Italy.jpg",
                            "https://www.youtube.com/watch?v=eajuMYNYtuY",
                            "http://www.imdb.com/title/tt0103064/?ref_=nv_sr_3")
edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "A journalist is caught in a time loop and must defeat an entire invading army himself to save mankind.",
                               "http://www.ramascreen.com/wp-content/uploads/2014/04/Edge-Of-Tomorrow-poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI",
                               "http://www.imdb.com/title/tt1631867/?ref_=fn_al_tt_1")
avatar = media.Movie("Avatar",
                     "FernGully, but on another planet in the future and in 3D. WARNING: Will make life seem less life-like.",
                     "http://fanaru.com/avatar/image/6676-avatar-avatar-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "http://www.imdb.com/title/tt0499549/?ref_=nv_sr_1")
inception = media.Movie("Inception",
                        "A thief who steals corporate secrets via dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://grimmella.files.wordpress.com/2012/09/inception-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",
                        "http://www.imdb.com/title/tt1375666/?ref_=nv_sr_1")
departed = media.Movie("The Departed",
                       "An undercover cop and a mole in the police department attempt to identify each other while infiltrating an Irish gang in South Boston.",
                       "http://www.freemovieposters.net/posters/departed_the_2006_1253_poster.jpg",
                       "https://www.youtube.com/watch?v=auYbpnEwBBg",
                       "http://www.imdb.com/title/tt0407887/?ref_=nv_sr_1")
toaster = media.Movie("The Brave Little Toaster",
                      "A toaster, a blanket, a lamp, a radio, and a vacuum cleaner journey to the city to find their master after being abandoned in their cabin in the woods.",
                      "http://media-cache-ec0.pinimg.com/736x/ec/f5/da/ecf5da8bd9f22fb0935d450e09d9f439.jpg",
                      "https://www.youtube.com/watch?v=bpGLpD25dpU",
                      "http://www.imdb.com/title/tt0092695/?ref_=nv_sr_2")

movies = [matrix, rush_hour, fellowship_of_the_ring, usual_suspects, anchorman,
          a_new_hope, judgement_day, edge_of_tomorrow, avatar, inception, departed, toaster]

fresh_tomatoes.open_movies_page(movies)
