
#need random and turtle
import random
import turtle

# Setup turtle for prog 3
win = turtle.Screen()
win.setup(1000, 1000)
win.title("Circles!")
win.bgcolor("white")
pete = turtle.Turtle()
pete.fillcolor("green")
pete.pencolor("black")
pete.speed(100)
pete.penup()
pete.hideturtle()

# Creating a random color function for prog 3	
def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]

# Creating a circle funtion for prog 3.
def drawCircle(xLoc, yLoc, fillColor):
    pete.setposition(xLoc, yLoc)
    pete.fillcolor(fillColor)
    pete.begin_fill()
    pete.circle(100)
    pete.end_fill()

xLoc = -400
yLoc = 400

for i in range(19):
    random_color = pick_color()
    drawCircle(xLoc,yLoc,random_color)
    xLoc = xLoc + 50
    yLoc = yLoc -50

xLoc = -400
yLoc = -400

for i in range(19):
    random_color = pick_color()
    drawCircle(xLoc,yLoc,random_color)
    xLoc = xLoc + 50
    yLoc = yLoc + 50
    
