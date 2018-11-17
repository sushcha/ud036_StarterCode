#import modules media and freshtomatoes
import media
import fresh_tomatoes

#create instances of class Movie from media.py taking in 4 attributes
toy_story = media.Movie("Toy Story", "Toys come to life", "http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

the_dark_knight = media.Movie("The Dark Knight", "Batman takes on the Joker", "https://images-na.ssl-images-amazon.com/images/I/81AJdOIEIhL._SY679_.jpg", "https://youtu.be/yQ5U8suTUw0")

argo = media.Movie("Argo", "Ben Affleck rescues US embassy employees from a country in riot", "https://images-na.ssl-images-amazon.com/images/I/51%2BW7gyGg4L.jpg", "https://youtu.be/JW3WfSFgrVY")

man_from_earth = media.Movie("The Man from Earth", "A departing professor tells his friends a secret", "https://images-na.ssl-images-amazon.com/images/I/71P53vTkaDL._RI_.jpg","https://youtu.be/lLfAW8KO6NE")

snatch = media.Movie("Snatch", "A caper involving a boxing promoter who is introduced to match fixing by a ruthless, pig-breeding gangster", "https://m.media-amazon.com/images/M/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTgxMTQtMWI1MGI0ZGQ5MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_.jpg", "https://youtu.be/ni4tEtuTccc")

sicario = media.Movie("Sicario", "The agency brings down a mexican jefe", "https://images-na.ssl-images-amazon.com/images/I/A10z3UREwrL._SY679_.jpg", "https://youtu.be/G8tlEcnrGnU")

#List of movies to be passed to function open_movies_page from freshtomatoes.py
movies = [toy_story, the_dark_knight, argo, man_from_earth, snatch, sicario]

#execute method open_movies_page
fresh_tomatoes.open_movies_page(movies)
