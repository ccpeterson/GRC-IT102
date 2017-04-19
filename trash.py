import turtle

# Setup window
win = turtle.Screen()
win.setup(500, 500)
win.title("Square ")
win.bgcolor("white")

# Setup the turtle attributes
pete = turtle.Turtle()
pete.shape("turtle")
pete.fillcolor("green")
pete.speed(100)

#function for a square
def drawSquare(xLoc,yLoc,sideLength,sqColor):

    #use the color
    pete.pencolor("black")

    # Move the turtle
    pete.penup()
    pete.goto(xLoc, yLoc)
    pete.pendown()
    pete.fillcolor(sqColor)
    pete.begin_fill()

    # Draw a square using a for loop
    for i in range(4) :
        pete.forward(sideLength)
        pete.right(90)

    pete.end_fill()


drawSquare(-200,200,100,"Blue")


