# petersonturtle.py
# Create and move a turtle object
# Clinton Peterson
# 12 April 2017

import turtle

# Setup window
win = turtle.Screen()
win.setup(500, 500)
win.title("Peterson Turtle")
win.bgcolor("white")

# Setup the turtle attributes
pete = turtle.Turtle()
pete.shape("turtle")
pete.fillcolor("green")
pete.pencolor("black")
pete.speed(1000)

#loop 60 times
#this number and the turn at the end need to have a product of 360 to make a full circle
for i in range(60):
#make  a crazy line out from center
    pete.forward(100)
    pete.right(40)
    pete.forward(50)
    pete.left(80)
    pete.forward(50)
    pete.right(40)
#pickup and prep for next line
    pete.penup()
    pete.setposition(0, 0)
    pete.pendown()
#turn 6 degrees do we can loop again
    pete.right(6)

#pander for votes    
pete.penup()
pete.setposition(-200, 200)
pete.fillcolor("red")
pete.pencolor("blue")
pete.write("VOTE PETERSON!!!", align="left", font=("Arial", 24, "normal"))

# Where is Pete?
print(pete.xcor())
print(pete.ycor())
print(pete.heading())

