from turtle import Turtle, Screen

# Create a turtle object from Turtle class
timmy = Turtle() 
print(timmy)

# change shape 
timmy.shape("turtle")

# change color
timmy.color("blue")

# Move the turtle forward
timmy.forward(100)

# Create a screen object and wait for a click
my_screen = Screen()
print("Canvas height:", my_screen.canvheight) # Get the height (attribute) of the screen canvas
my_screen.exitonclick()