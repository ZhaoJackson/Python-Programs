import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(f"your choice is {game[user_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose {game[computer_choice]}")

# construct game rule
# 0: rock, 1: paper, 2: scissors
# rock > scissors, scissors > paper, paper > rock

# make sure user_choice and computer_choice are valid
if user_choice >= 3 and user_choice < 0:
    print("You typed an invalid number, you lose!")

# 2 typical cases before comparsion (paper > rock)
# if you choose rock and computer choose scissors, you win
elif user_choice == 0 and computer_choice == 2:
    print("You win!")

# if you choose scissors and computer choose rock, you lose
elif computer_choice == 0 and user_choice == 2:
    print("You lose")

# apart from paper and rock, the larger value wins
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")

# if user_choice == computer_choice, it's a draw
elif computer_choice == user_choice:
    print("It's a draw")
else:
    print("You typed an invalid number, you lose!")