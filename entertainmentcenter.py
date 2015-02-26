import media
import fresh_tomatoes

#create instances of movie. The movie takes four inputs: title, storyline, link address of trailer video, link address of poster
gladiator = media.Movie(
    'Gladiator',
    'The general who becomes a slave, the slave who becomes a gladiator, the gladiator who defines an empiror.',
    'https://www.youtube.com/watch?v=ol67qo3WhJk',
    'http://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg'
    )


incredibles = media.Movie(
    'The Incredibles',
    'A family of superheros gets on a mission to beat a science villan.',
    'https://www.youtube.com/watch?v=1LASc8ewLaw',
    'http://img3.wikia.nocookie.net/__cb20100622151355/pixar/images/4/44/Movie_poster_the_incredibles.jpg'
    )


johnwick = media.Movie(
    'John Wick',
    'The retired killer gets his revenge against the ones that hurt his loved ones.',
    'https://www.youtube.com/watch?v=2AUmvWm5ZDQ',
    'http://i.imgur.com/nFtglna.jpg'
    )


family = media.Movie(
    'The Family',
    'A retired mafia leader and his family move to a small French town, where things become interesting',
    'https://www.youtube.com/watch?v=nwZNypYmPFE',
    'http://upload.wikimedia.org/wikipedia/en/7/75/The_Family_2013%2C_Poster.jpg'
    )


interstellar = media.Movie(
    'Interstellar',
    'Human is near distinction, and NASA is sending astronauts through a worm-hole to find new planets to live in.',
    'https://www.youtube.com/watch?v=0vxOhd4qlnA',
    'http://img2.wikia.nocookie.net/__cb20141003183252/interstellarfilm/images/b/bd/Interstellar-2014-Movie-Poster.jpg'
    )


porco_rosso = media.Movie(
    'Porco Rosso',
    'The famous pilot, Porco Rosso, who turned into a red pig by a curse, getts challenged by an American pilot for his glory and love.',
    'https://www.youtube.com/watch?v=awEC-aLDzjs',
    'http://images.moviepostershop.com/porco-rosso-movie-poster-1992-1020670123.jpg'
    )
    

movies=[gladiator, incredibles, johnwick, family, interstellar, porco_rosso]   #arrange the movie information into a list of object

fresh_tomatoes.open_movies_page(movies)  #fesh_tomatoes creates the movie page using the movies information created in this page.


