import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)

lives = 6

# random choice from computer
chosen_word = random.choice(word_list)

# create placeholder for user to guess
place_holder = ''
for _ in range(len(chosen_word)):
    place_holder += '_'
print("Word to guess: " + place_holder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("What letter of your guess? ").lower()

    if guess in correct_letters:
        print(f"you have already chosen letter {guess}, use different one")

    display = ''
    
    for letter in chosen_word:

        if guess == letter:
            display += guess

            correct_letters.append(guess) # used for check

        elif letter in display:
            display += letter

        else:
            display += '_'
    print("Word to guess " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word, use different one")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

        if '_' not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(stages[lives])