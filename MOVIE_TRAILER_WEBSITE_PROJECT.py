# Imports the media file, where the class Movie is held.
import media

# Imports the fresh_tomatoes file,
# where the movie website is actually created
import fresh_tomatoes

# Below, each of my 6 favorite movies is created
# as an instance of class "Movie", inside file "media".
IaWL = media.Movie(
    "It's a Wonderful Life",
    "Story of troubled, kindhearted man saved by his guardian angel",
    "http://scriptshadow.net/wp-content/uploads/" +
    "2013/12/itsawonderfullife-email.jpg",
    "https://www.youtube.com/watch?v=LJfZaT8ncYk")

Dark_Knight = media.Movie(
    "The Dark Knight",
    "Batman deals with latest nefarious Joker scheme",
    "http://www.gortoncenter.org/film/all/image/z8uD1KXF63lpy8TT2A4kOVh9H" +
    "ScO5y5qfV9igmoH-z6INSEwULLqfZsMubFB8Mg9zPUw300.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

Lego_Movie = media.Movie(
    "Lego Movie",
    "Average lego dude uses help from new friends to defeat the bad guy",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4MDk1ODEx" +
    "N15BMl5BanBnXkFtZTgwNzIyNjg3MDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

Star_Wars_6 = media.Movie(
    "Star Wars 6",
    "Good guys destroy death star (again)",
    "https://vignette2.wikia.nocookie.net/starwars/" +
    "images/9/94/Ep6DVD.jpg/revision/latest?cb=20060430133003",
    "https://www.youtube.com/watch?v=5UfA_aKBGMc")

Inception = media.Movie(
    "Inception",
    "Dreams inside dreams",
    "https://upload.wikimedia.org/wikipedia/en/" +
    "2/2e/Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=66TuSJo4dZM")

Looper = media.Movie(
    "Looper",
    "Time traveling killer meets future self, amid other conflicts",
    "http://www.sonypictures.com/movies/looper/assets/images/onesheet.jpg",
    "https://www.youtube.com/watch?v=2iQuhsmtfHw")

# List of movies inserted into a list called "movies"
movies = [IaWL, Dark_Knight, Lego_Movie, Star_Wars_6, Inception, Looper]

# Then, the list of movies is passed into the
# fresh_tomatoes file, which generates the website.
fresh_tomatoes.open_movies_page(movies)
