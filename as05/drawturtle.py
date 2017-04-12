# drawturtle.py
# Create and move a turtle object
# Rich Bankhead
# 09 January 2016

import turtle

# Setup window
win = turtle.Screen()
win.setup(800, 800)
win.title("Draw Turtle")
win.bgcolor("white")

# Setup the turtle attributes
alex = turtle.Turtle()
alex.shape("turtle")
alex.fillcolor("green")
alex.pencolor("black")
alex.speed(0) 

# Move the turtle
alex.penup()
alex.goto(-250, +250)
alex.pendown()

# Draw a square
alex.forward(150)
alex.right(90)
alex.forward(150)
alex.right(90)
alex.forward(150)
alex.right(90)
alex.forward(150)
alex.right(90)

# Move the turtle
alex.penup()
alex.goto(+50, -50)
alex.pendown()

# Draw a square using a for loop
for i in range(4) :
    alex.forward(150)
    alex.right(90)

# Move the turtle
alex.penup()
alex.goto(0, -50)
alex.pendown()


# Draw a circle and fill it.
alex.fillcolor("red")
alex.begin_fill()
alex.circle(100)
alex.end_fill()


# Where is Alex?
print(alex.xcor())
print(alex.ycor())
print(alex.heading())


