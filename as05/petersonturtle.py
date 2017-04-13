# petersonturtle.py
# Create and move a turtle object
# Clinton Peterson
# 12 April 2017

import turtle

# Setup window
win = turtle.Screen()
win.setup(500, 500)
win.title("Peterson Turtle! VOTE FOR ME!")
win.bgcolor("white")

# Setup the turtle attributes
pete = turtle.Turtle()
pete.shape("turtle")
pete.fillcolor("green")
pete.pencolor("black")
pete.speed(100)

#loop 60 times
#this number and the turn at the end need to have a product of 360 to make a full circle
for i in range(60):
#make a crazy line out from center
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
pete.setposition(-150, 200)
pete.fillcolor("red")
pete.pencolor("blue")
pete.write("VOTE PETERSON!!!", align="left", font=("Arial", 24, "normal"))

#do a little dance
for i in range(20):
    pete.right(45)
    pete.forward(10)
    pete.left(90)
    pete.forward(10)
    pete.right(45)

#another stationary color dance
for i in range(20):
    pete.fillcolor("yellow")
    pete.right(45)
    pete.fillcolor("pink")
    pete.right(45)    

# Where is Pete?
print("Little Pete's final loaction: X", pete.xcor(),"Y", pete.ycor(), "Heading", pete.heading())
print()
print("VOTE FOR PETERSON!")

