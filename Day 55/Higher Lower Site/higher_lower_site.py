from flask import Flask
import random

# Create the server
app = Flask(__name__)

# Create the site
@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Gif">'

# Generate the number
number = random.randint(0, 9)

# Use the user's input 
@app.route('/<int:guess>')
def guess_number(guess):
    if guess < number:
        return '<h1 style="color: red;">Too low!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Gif">'
    elif guess > number:
        return '<h1 style="color: blue;">Too high!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Gif">'
    else:
        return '<h1 style="color: green;">Just right!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Gif">'

# Add the main driver function
if __name__ == "__main__":
    app.run(debug=True)
