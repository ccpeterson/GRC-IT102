# threeBallBounce.py
# Clinton Peterson
# 16 May 2017


from graphics import *
import random

#Define Constants
WIN_WIDTH = 800   #Pixels
WIN_HEIGHT = 800  #Pixels
UPDATE_RATE = 60 #Frames per second
BALL_RAD = 50


#Setup graphics window object
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")

#Setup up the balls

ball01 = Circle(Point(WIN_WIDTH//2 ,WIN_HEIGHT/2), BALL_RAD)
ball01.setFill("blue")
ball01.setOutline("black")
ball01.setWidth(5)
ball01.draw(win)

def up():
    ball01.move(0, -30 * moveY)


moveY = 5

yDir1 = 1


#Main Program
while True:
    key = win.checkKey()
    if key == "space":
        up()

    if ball01.getCenter().getY() > WIN_HEIGHT - BALL_RAD :
        ball01.setFill("red")
        break
    
    ball01.move(0, moveY*yDir1)
        
    update(UPDATE_RATE)




