from art import logo

# Operation
# Addition
def add(n1, n2):
    return n1 + n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Division
def divide(n1, n2):
    return n1 / n2

# Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operation = {}
operation["+"] = add
operation["-"] = subtract
operation["*"] = multiply
operation["/"] = divide

def calculator():
    print(logo)
    should_accumulate = True
    # Program asks the user to type the first number.
    # Since it may be re-used later, it cannot be involved inside the while loop from overwriting
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        # Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
        for sym in operation:
            print(sym)
        operation_symbol = input("Pick an operation: ")

        # Program asks the user to type the second number.
        num2 = float(input("What's the next number?: "))

        # Program works out the result based on the chosen mathematical operator.
        result = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        # Program asks if the user wants to continue working with the previous result.
        want_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
        if want_continue == "y":
            num1 = result
        
        # If no, program asks the user for the fist number again and wipes all memory of previous calculations.
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() # restart from beginning: recursion

calculator()