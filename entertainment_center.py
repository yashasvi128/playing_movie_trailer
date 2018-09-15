import fresh_tomatoes  # user defined library
import media  # user defined library

print(media.Movie.__doc__)

toy_story = media.Movie(  # instance of class video and movie is created
    "Toy Story",
    "1h 34m",
    "A story of a boy and his toys that come to life",
    "https://goo.gl/MAevYU",
    "https://www.youtube.com/watch?v=rNk1Wi8SvNc"
)  # values are passed
print(toy_story.title)
print(toy_story.movie_duration)
print(toy_story.storyline)

avatar = media.Movie(  # instance of class video and movie is created
    "Avatar",
    "2h 42m",
    "A marine on an alien planet",
    "https://goo.gl/iUkKRm",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)  # values are passed
print(avatar.title)
print(avatar.movie_duration)
print(avatar.storyline)

inception = media.Movie(  # instance of class video and movie is created
    "Inception",
    "2h 28m",
    "Dream within a dream to plant an idea",
    "https://goo.gl/mtJqeT",
    "https://www.youtube.com/watch?v=8hP9D6kZseM"
)  # values are passed
print(inception.title)
print(inception.movie_duration)
print(inception.storyline)

ratatouille = media.Movie(  # instance of class video and movie is created
    "Ratatouille",
    "1h 51m",
    "A rat that cooks delicious food",
    "https://goo.gl/YcACW7",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
)  # values are passed
print(ratatouille.title)
print(ratatouille.movie_duration)
print(ratatouille.storyline)

gravity = media.Movie(  # instance of class video and movie is created
    "Gravity",
    "1h 31m",
    "A story about the medical engineer's shuttle mission",
    "https://goo.gl/Th8wKL",
    "https://www.youtube.com/watch?v=k0ijEEivCbg"
)  # values are passed
print(gravity.title)
print(gravity.movie_duration)
print(gravity.storyline)

the_imitation_game = media.Movie(  # instance of class video & movie is created
    "The Imitation Game",
    "1h 54m",
    "A story based on the work of Allen Turing",
    "https://upload.wikimedia.org/wikipedia/en/8/87/The_Imitation_Game_%282014%29.png",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM"
)  # values are passed
print(the_imitation_game.title)
print(the_imitation_game.movie_duration)
print(the_imitation_game.storyline)

movies = [toy_story, avatar, inception, ratatouille, gravity,
          the_imitation_game]  # array is defined
fresh_tomatoes.open_movies_page(movies)  # array is passed to fresh_tomatoes
