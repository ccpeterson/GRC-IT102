# snake.py
# Clinton Peterson
# 25 May 2017

from graphics import *
import random

WIN_WIDTH = 1100 #Pixels
WIN_HEIGHT = 1100 #Pixels
UPDATE_RATE = 4 #frames per second
BALL_SIZE = 20 #ball Size in Pixels
BALL_OUTLINE = 2 #width of ball border in pixels
NUM_BALLS = 100 #how many balls

#Setup graphics window object
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("white")

#create balls, from top left moving down
ballList = []
for i in range (NUM_BALLS):
    ballList.append(Circle(Point(4*BALL_SIZE,4*BALL_SIZE + i*2*BALL_SIZE), BALL_SIZE))
    ballList[i].setFill("green")
    ballList[i].setWidth(BALL_OUTLINE)
    ballList[i].draw(win)

#move the balls, starting to the right
moveDir = [1,0]
while True:
    key = win.checkKey()        
    if key == "Up" and moveDir != [0,1]:
        moveDir = [0,-1]
    elif key == "Down" and moveDir != [0,-1]:
        moveDir = [0,1]
    elif key == "Left" and moveDir != [1,0]:
        moveDir = [-1,0]
    elif key == "Right" and moveDir != [-1,0]:
        moveDir = [1,0]
    for i in range (NUM_BALLS - 1):
        ballList[NUM_BALLS-1-i].move(ballList[NUM_BALLS-2-i].getCenter().getX()-ballList[NUM_BALLS-1-i].getCenter().getX(),0)
        ballList[NUM_BALLS-1-i].move(0,ballList[NUM_BALLS-2-i].getCenter().getY()-ballList[NUM_BALLS-1-i].getCenter().getY())
    ballList[0].move(moveDir[0]*2*BALL_SIZE,moveDir[1]*2*BALL_SIZE)
    update(UPDATE_RATE)
