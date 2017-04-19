# polygon.py
# drawing stuff
# Clinton Peterson
# 19 April 2017

#need random and turtle
import random
import turtle

# Setup window
win = turtle.Screen()
win.setup(800, 800)
win.title("Polygons are crazy!")
win.bgcolor("white")

# Setup the turtle attributes
pete = turtle.Turtle()
pete.fillcolor("green")
pete.pencolor("black")
pete.speed(100)
pete.penup()
pete.hideturtle()

# Define the draw function
def drawPolygon(numSides, lenSides, xLoc, yLoc, fillColor):
	#set the turn angle
	turnAngle = (360/numSides)
	
	#goto the start
	pete.setposition(xLoc, yLoc)
	
	#set color
	pete.fillcolor(fillColor)
	
	#make the shape
	pete.pendown()
	pete.begin_fill()
	for i in range(numSides):
		pete.forward(lenSides)
		pete.right(turnAngle)
	pete.end_fill()
	pete.penup()

# Creating a random color function	
def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]
	
#Making 25 random shapes
for i in range(25):
	# setting the random attributes
	sideRandom = (random.randint(3,10))
	lenRandom = (random.randint(10,100))
	xRandom = (random.randint(-300,300))
	yRandom = (random.randint(-300,300))	
	random_color = pick_color()
	# doing the thing
	drawPolygon(sideRandom,lenRandom,xRandom,yRandom,random_color)

	
	
