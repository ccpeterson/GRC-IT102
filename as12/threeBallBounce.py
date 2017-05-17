# threeBallBounce.py
# Clinton Peterson
# 16 May 2017


from graphics import *
import random

#Define Constants
WIN_WIDTH = 800 #Size of window in pixels
WIN_HEIGHT = 800 #Size of window in pixels
UPDATE_RATE = 60 #Frames per second
BALL_RAD = 50 #Size of ball in pixels
MOVEX = 5 #Movement per frame in pixels


#Setup graphics window object
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")

#Setup up the balls
ball01 = Circle(Point(WIN_WIDTH//2 - 100,WIN_HEIGHT/2), BALL_RAD)
ball01.setFill("red")
ball01.setOutline("black")
ball01.setWidth(5)
ball01.draw(win)

ball02 = Circle(Point(WIN_WIDTH//2 + 100,WIN_HEIGHT/2), BALL_RAD)
ball02.setFill("blue")
ball02.setOutline("black")
ball02.setWidth(5)
ball02.draw(win)

ball03 = Circle(Point(WIN_WIDTH//2 + 300,WIN_HEIGHT/2), BALL_RAD)
ball03.setFill("green")
ball03.setOutline("black")
ball03.setWidth(5)
ball03.draw(win)

#Initial direction of the movement
xDir1 = -1
xDir2 = 1
xDir3 = -1

#Main Program
while True:
    #If Ball 1's x cord is within a radius of the wall, reverse its direction
    if ball01.getCenter().getX() > WIN_WIDTH-BALL_RAD or ball01.getCenter().getX() < BALL_RAD:
        xDir1 *= -1        

    #If Ball 2's x cord is within a radius of the wall, reverse its direction
    if ball02.getCenter().getX() > WIN_WIDTH-BALL_RAD or ball02.getCenter().getX() < BALL_RAD:
        xDir2 *= -1

    #If Ball 3's x cord is within a radius of the wall, reverse its direction
    if ball03.getCenter().getX() > WIN_WIDTH-BALL_RAD or ball03.getCenter().getX() < BALL_RAD:
        xDir3 *= -1        

    #If ball 1 and 2's x cords are within 2 radius of each other, switch both of their directions
    if abs(ball01.getCenter().getX() - ball02.getCenter().getX()) < 2*BALL_RAD:
        xDir1 *= -1
        xDir2 *= -1

    #If ball 3 and 2's x cords are within 2 radius of each other, switch both of their directions    
    if abs(ball03.getCenter().getX() - ball02.getCenter().getX()) < 2*BALL_RAD:
        xDir3 *= -1
        xDir2 *= -1

    #Move the balls
    ball01.move(MOVEX*xDir1, 0)
    ball02.move(MOVEX*xDir2, 0)
    ball03.move(MOVEX*xDir3, 0)

    #Draw the screen
    update(UPDATE_RATE)
