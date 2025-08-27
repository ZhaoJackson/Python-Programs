from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects of each class
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# step 1: print report
# display report from money machine by object.method
money_machine.report()
coffee_maker.report()

# activate while loop
is_on = True

# step 2: check resources sufficient
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ") # Prompt user by input function
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice) # Get the selected drink from the menu through object.method

        # step 3: process coin
        if coffee_maker.is_resource_sufficient(drink):

            # step 4: check transaction successful
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)