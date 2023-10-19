from art import logo, vs
from game_data import data
import random

# TODOS:
# [x] Print the logo of the game
# [] Create a function that returns a random item from 'data'
# [x] Create a global var to save the current score
# [] Save in a 'itemA' var a random item
# [] Print the VS logo
# [] Save in a 'itemB' var a random item
# [] Ask user for a guess
# [] Create a function that compares the number of followers of 2 items
# [] Check user's guess
# [] Print the result and end the game if player fails
# [] Print the result and change item vars if player get's right

# Create a function that returns a random item from 'data'
def get_random_item():
    return data[random.randint(0, len(data) - 1)]

# Global variables
score = 0

# Print the logo of the game
print(logo)