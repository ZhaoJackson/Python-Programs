# The objective is to take the inputs from the user to these questions and then generate a random password. 

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
# 4 letters 2 symbols and 3 numbers
# all the letters are together. All the symbols are together and all the numbers follow each other as well. 

password = ""
for _ in range(1, nr_letters + 1): # The loop does not use the variable char inside the loop body. 
    # However, char is still important because it determines how many times the loop runs. It will run 4 times
    random_char = random.choice(letters)
    password += random_char 

for _ in range(1, nr_symbols + 1): # run symbol 2 times
    random_sym = random.choice(symbols) # store each symbols and append to the password string
    password += random_sym

for _ in range(1, nr_numbers + 1): # run number 3 times
    random_num = random.choice(numbers)
    password += random_num

print(f"your password is {password}")

# Hard Version
# In the advanced version of this project the final password does not follow a pattern.
# every time you generate a password, the positions of the symbols, numbers, and letters are different. 

password = [] # use list to store the items for later shuffle
for _ in range (1, nr_letters + 1): # same logic as above
    random_char = random.choice(letters)
    password.append(random_char) # use append to add items to the list

for _ in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    password.append(random_sym)

for _ in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password.append(random_num)

random.shuffle(password) # random.shuffle(list) can randomly arrange any position of item

passcode = '' # convert the shuffled list to the string
for key in password:
    passcode += key # use string contantenation to add each item to the string
print(f"your password is {passcode}")


# string adding:
string = ''
for i in string:
    string += i
print(string) # output: ''


# list adding
original_list = [1, 2, 3]
new_list = []
for i in original_list:
    new_list.append(i)
print(new_list) # output: [1, 2, 3]


# dictionary adding
students = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
student_dict = {}

for i in range(len(students)):
    student_dict[students[i]] = scores[i]
print(student_dict) # output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}