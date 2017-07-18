import media
import fresh_tomatoes

# creation of each of my favorite movies from class movie defined on media.py
rio = media.Movie("Rio", "A group of birds out of the african jungle",
                        "https://upload.wikimedia.org/wikipedia/en/b/bb/Rio2011Poster.jpg",
                        "https://www.youtube.com/watch?v=P1GRO31ve5Q")


civil_war = media.Movie("Captain America: civil war", "Captain America against Iron Man",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                     "https://www.youtube.com/watch?v=FkTybqcX-Yo")
                     


strange = media.Movie("Doctor Strange", "A medical with supernatural power",
                      "https://upload.wikimedia.org/wikipedia/en/4/4f/Doctor_Strange_Vol_4_2_Ross_Variant_Textless.jpg",
                      "https://www.youtube.com/watch?v=HSzx-zryEgM")

furious_8 = media.Movie("Furious 8", "Dom with Cipher against his former teammates",
                        "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                        "https://www.youtube.com/watch?v=uisBaTkQAEs")

# List movies will hold all the movie objects above
movies = [rio, civil_war, furious_8, strange]

"""Call to the function open_movies_page to display the web page with all the movies
by passing my list of movies"""

fresh_tomatoes.open_movies_page(movies)

                      


