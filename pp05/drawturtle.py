# drawturtle.py
# Create and move a turtle object
# Clinton and Aksh
# 11 April 2017

import turtle

# Setup window
win = turtle.Screen()
win.setup(800, 800)
win.title("Turtle stuff")
win.bgcolor("grey")

# Setup the 1st turtle attributes
clint = turtle.Turtle()
clint.shape("turtle")
clint.fillcolor("blue")
clint.pencolor("black")
clint.speed(5) 

# Move the turtle
clint.penup()
clint.goto(-250, +250)
clint.pendown()

# Draw a square using a for loop
for i in range(4) :
    clint.forward(150)
    clint.right(90)
	
# Setup the 2nd turtle attributes
aksh = turtle.Turtle()
aksh.shape("turtle")
aksh.fillcolor("red")
aksh.pencolor("black")
aksh.speed(5) 

# Move the turtle
aksh.penup()
aksh.goto(0, 250)
aksh.pendown()

# Draw a square using a for loop
for i in range(4) :
    aksh.forward(150)
    aksh.right(90)

#Draw a circle and fill it.
aksh.fillcolor("red")
aksh.begin_fill()
aksh.circle(100)
aksh.end_fill() 
	
#Draw a square
aksh.forward(150)
aksh.right(90)
aksh.forward(150)
aksh.right(90)
aksh.forward(150)
aksh.right(90)
aksh.forward(150)
aksh.right(90)

# Move the turtle
# alex.penup()
# alex.goto(+50, -50)
# alex.pendown()



# Move the turtle
# alex.penup()
# alex.goto(0, -50)
# alex.pendown()


# Draw a circle and fill it.
# alex.fillcolor("red")
# alex.begin_fill()
# alex.circle(100)
# alex.end_fill()


# Where is Clint?
print(clint.xcor())
print(clint.ycor())
print(clint.heading())


