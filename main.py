from art import logo, vs
from game_data import data
import random
import os

# TODOS:
# [x] Print the logo of the game
# [x] Create a function that returns a random item from 'data'
# [x] Create a global var to save the current score
# [x] Save in a 'itemA' var a random item
# [x] Print the VS logo
# [x] Save in a 'itemB' var a random item
# [x] Ask user for a guess
# [x] Create a function that compares the number of followers of 2 items
# [x] Check user's guess
# [x] Print the result and end the game if player fails
# [x] Print the result and change item vars if player get's right

# Clear console function (works on Windows and Linux)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Create a function that returns a random item from 'data'
def get_random_item():
    return random.choice(data)

# Create a function that compares the number of followers of 2 items (returns True if 'item1' has more followers)
def has_more_followers(item1, item2):
    return item1['follower_count'] > item2['follower_count']

# Global variables
score = 0
player_has_guessed = False

# Main loop
while True:
    # Declare a variable to save player's answer
    player_guess = ''

    # Print the logo of the game
    print(logo)

    # If 'score' > 0 print success and score
    if score > 0:
        print(f"You're right! Current score: {score}.")
        # Make itemB to be itemA
        itemA = itemB
    else:
        # Save in a 'itemA' var a random item
        itemA = get_random_item()

    # Print item A info
    print(f"Compare A: {itemA['name']}, a {itemA['description']}, from {itemA['country']}")

    # Print the VS logo
    print(vs)

    # Save in a 'itemB' var a random item
    itemB = get_random_item()

    # Print item B info
    print(f"Against B: {itemB['name']}, a {itemB['description']}, from {itemB['country']}")

    # Ask user for a guess
    while player_guess != 'A' and player_guess != 'B':
        player_guess = input("Who has more followers? Type 'A' or 'B': ")

    # Check user's guess
    if player_guess == 'A':
        player_has_guessed = has_more_followers(itemA, itemB)
    else:
        player_has_guessed = has_more_followers(itemB, itemA)

    if not player_has_guessed:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    else:
        score += 1
        clear_console()