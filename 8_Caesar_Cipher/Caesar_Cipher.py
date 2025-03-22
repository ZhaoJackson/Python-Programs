from art import logo
print(logo)

# Set the alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# combine the encrypt and decrypt processes
def caesar(original_text, shift_amount, direction):

    # set the empty string
    output_text = ''

    # manipulate the shift amount direction based on demand of encode or decode
    if direction == 'decode': 
        shift_amount *= -1 # -1 if decode and move the shift of each letter leftwards
    else:
        shift_amount *= 1 # 1 if encode and move the shift letter rightwards
    
    # process encode or decode letters
    for letter in original_text:

        # make sure non-letter symbols remain unchanged
        if letter not in original_text:
            output_text += letter
        
        # proceed shifting based on each letter's alphabet position and shift collectively in either direction (-1 or 1)
        else:
            shift_position = alphabet.index(letter) + shift_amount # get the shift number based on each letter position and required shift amount with direction
            shift_position %= len(alphabet) # make sure the letter at the end can return to the beginning
            output_text += alphabet[shift_position] # return the shift number as index in the alphabet list and append to the empty string

    print(f"Here is the {direction} result: {output_text}.")

# Restarting the session
should_continue = True # assume the game keeps going forever

# set the main while loop with input query and function caller afterwards
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # the caller follows the input since it needs to inside and process above function
    caesar(original_text = text, shift_amount = shift, direction = direction)

    # ask user to continue or no
    restart = input("Do you still want to continue? Type yes or no.").lower()
    if restart == "yes": # if continue, the while loop still keep running from beginning
        should_continue = True
        print("Let's have another round:)")
    else: # if stop, the while loop condition is false, then it will stop
        should_continue = False
        print("Goodbye:)")



















