from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against the actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
    
# Function to set the difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Function to play the number guessing game
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    turns = set_difficulty()
    
    # Repeat the guessing process if they get it wrong
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # let user guess a number
        guess = int(input("Make a guess: "))
        
        # track the number of turns and reduce by 1 if the guess is wrong
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        
        elif guess != answer:
            print("Guess again.")

# Main function to run the game
if __name__ == "__main__":
    play_game()