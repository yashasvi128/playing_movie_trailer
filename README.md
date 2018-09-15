## **MOVIE TRAILER WEBSITE**
### **INTRODUCTION:**
A server-side code that stores the list of movies, including box art imagery and the movie trailer URL. Then use the code to generate a static web page allowing visitors to review their movie and watch trailer by just clicking on the poster of the movie.

### Requirements:
1. Installation of Python. For downloading Python, Visit: https://www.python.org/downloads/
  - In this project Python 2.7 (64-bit ) was used.
2. Basic knowledge of Python and HTML Syntax.

### Attached Files:
1. The file  fresh_tomatoes.py contains the _open_movies_page()_ function that will take in the list of movies, that  you want to display, and generate an HTML file including the content provided by you, producing a website to showcase your entered movies.
2. In media.py a class video is defined with the properties of a video like:  movie title, duration of the movie. Another class movie is defined with some of the inherited properties of class video; and including other properties of movie like: movie storyline, poster image and movie trailer URLs.
3. A list of the movie objects is stored in entertainment_center.py. By calling the constructor media.Movie() to instantiate movie objects we pass movies their own custom data structure by defining the video class, movie class and constructor, and now these objects can be stored in a list data structure.

### Get to the Code and Check for Errors:
 - To obtain the code, right click on the file with .py extension and choose edit with IDLE.
 - To check for errors, press F5 or go to Run Menu and choose Run Module. Errors, if any will appear in the shell Window.

### How to Run the Application:
 ##### Using the Terminal:
 - Type python entertainment_center.py file. Movie Trailer Website will show up.
 ##### Using the Python IDLE:
 - Select Run from the IDLE menu.
 - Click Run Module from the dropdown list.

 #### Note: fresh_tomatoes.py_ and entertainment_center.py must be stored in the same folder.

### Expected Output:
1. HTML page opens up in the web browser, listing all the movies that you have added.
Click on any movie poster to view its trailer.
2. Title, story line and duration of the movie is printed in the shell.
