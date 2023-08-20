import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("#d00")  # Set the background color

# Create a turtle
draw = turtle.Turtle()

# Setup turtle for drawing circle
draw.speed(5) # Set the pen speed
draw.pensize(10) # Set the line width to 10 pixels
draw.pencolor("white") # Set the pen color to white

# Move the turtle to the coordinate x = 0 and y = -200
draw.penup() # Lift the pen to move without drawing
draw.goto(0, -200) # Adjust the Y-coordinate to position the circle in the middle
draw.fillcolor("white") # Set the fill color to white
draw.begin_fill() # Start filling

# Draw a circle
draw.pendown()
draw.circle(200)
draw.end_fill() # End filling
draw.penup()  # Lift the pen to move without drawing

# Setup turtle for drawing nazi logo
draw.pencolor("black") # Set the pen color to black
draw.goto(140 - 65, 170 - 65)  # Move the turtle to the top-left inside the circle with 65 pixels gap
draw.setheading(45) # Set the initial angle to 45 degrees (diagonal direction)
draw.fillcolor("black") # Set the fill color to black
draw.begin_fill() # Start filling

# Draw the diagonal rectangle
draw.pendown()

# Draw the symbol from top right
draw.right(90) # Turn 90 degrees
draw.forward(150)  # Length of the diagonal
draw.right(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.right(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal
draw.left(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.left(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal

# Draw the next bottom right symbol
draw.right(90) # Turn 90 degrees
draw.forward(150)  # Length of the diagonal
draw.right(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.right(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal
draw.left(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.left(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal

# Draw the next bottom left symbol
draw.right(90) # Turn 90 degrees
draw.forward(150)  # Length of the diagonal
draw.right(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.right(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal
draw.left(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.left(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal

# Draw the next top left symbol
draw.right(90) # Turn 90 degrees
draw.forward(150)  # Length of the diagonal
draw.right(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.right(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal
draw.left(90) # Turn 90 degrees
draw.forward(50) # Width of the rectangle
draw.left(90) # Turn 90 degrees
draw.forward(100) # Length of the diagonal

draw.end_fill() # End filling
draw.penup()  # Lift the pen to move without drawing

# Hide turtle from screen
draw.hideturtle()

# Keep the window open until it's manually closed
turtle.done()
