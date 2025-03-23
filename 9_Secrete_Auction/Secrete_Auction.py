# Functionality
# Each person writes their name and bid.
# The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
# Each person's name and bid are saved to a dictionary.
# Once all participants have placed their bid, the program works out who has the highest bid and prints it.


from art import logo
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] # store the bidder with their bid_amount in the dictionary
        if bid_amount > highest_bid:
            highest_bid = bid_amount # set the highest bid
            winner = bidder # set the key corresponding to its name as winner
    print(f"The winner is {winner} with a highest bid {highest_bid}")

bids = {} # it will be function parameter

# use while loop to continue or stop looping
continue_bidding = True
while continue_bidding:
    # set the key
    name = input("What is your name? ").lower()
    # set the value
    price = int(input("what is your bid? "))

    # store the key: value as {name: price}
    bids[name] = price

    # grant the switch to continue or stop
    should_continue = input("Are there any other bidder? Type yes or no").lower()
    if should_continue == 'no':
        continue_bidding = False # while loop will stop

        # call the function and show the winner with bid
        find_highest_bidder(bidding_record = bids)

    else:
        print("\n" * 20)