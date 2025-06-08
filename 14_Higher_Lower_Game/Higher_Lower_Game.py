from art import logo, vs
from data import data
import random

def format_data(account):
    """Format the account data into printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."

def check_answer(guess, a_follower_count, b_follower_count):
    """Check if the user's guess is correct."""
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_should_continue = True

# Generate a random account from the data
account_b = random.choice(data)

# Make the game loop
while game_should_continue:

    # Making account at position B become the next account at position A
    account_a = account_b
    # Generate a new random account from the data
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print ("\n" * 20)
    print(logo)

    # get follower counts
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    # check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give feedback on user's guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")