# 0x04. AirBnB clone - Web framework

## Web app framework - Architecture

* Model - The model comprises of all the data, business logic layers
its guidelines and functions.The model upon getting user input data
from the controller , tells the way an updated interface should be
displayed directly to the views

# Tasks

5. Number template

* Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
* The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
* H1 tag: “Number: n” inside the tag BODY
* You must use the option strict_slashes=False in your route definition
