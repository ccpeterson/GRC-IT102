# flappyBall2.py
# Clinton Peterson
# 18 May 2017

from graphics import *
import random

#Define Constants
WIN_WIDTH = 1000 #Pixels
WIN_HEIGHT = 1000 #Pixels
UPDATE_RATE = 60 #frames per second
BALL_RAD = 30 #ball Size in Pixels
MOVEX = 2 #Pipe's moving left speed
MOVEY = 2 #Falling speed in pixels per frame
PIPE_LENGTH = 300 #in pixels, from floor and ceiling
PIPE_WIDTH = 50 #in pixels

#Setup graphics window object
win = GraphWin("Flappy Ball", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")

#Setup up the ball
ball01 = Circle(Point(200 ,WIN_HEIGHT/2), BALL_RAD)
ball01.setFill("blue")
ball01.setOutline("black")
ball01.setWidth(5)
ball01.draw(win)

#Setup the pipe lists
topPipeList = []
bottomPipeList = []

#Setup the pipe function
def makePipes(lvl):
    topPipeList.append(Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,0), Point(WIN_WIDTH,PIPE_LENGTH)))
    topPipeList[lvl].setFill("green")
    topPipeList[lvl].setOutline("black")
    topPipeList[lvl].draw(win)
    bottomPipeList.append(Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,WIN_HEIGHT), Point(WIN_WIDTH,WIN_HEIGHT-PIPE_LENGTH)))
    bottomPipeList[lvl].setFill("green")
    bottomPipeList[lvl].setOutline("black")
    bottomPipeList[lvl].draw(win)

message = Text(Point(500,100), "Hello!")

#setting variable to be changed when you lose or win a level
gameOver = 0
level = 0

#Main Program Loop
while True:
    #if level loop was broken becuase you lost, stop
    if gameOver == 1:
        break
    #Draw the pipes
    makePipes(level)
    #This sets a variable to be the same as the x cord of the leading edge of the pipe
    xPipe = WIN_WIDTH - PIPE_WIDTH
    #resets the win counter
    winner = 0
    #Loop for each level
    while True:
        #Setting a variable for key presses
        key = win.checkKey()
        #For every space bar it flaps up 20 times what it falls each frame
        if key == "space":
            ball01.move(0, -20 * MOVEY)
        #If the ball hits the top bottom, gameover
        if ball01.getCenter().getY() + BALL_RAD >= WIN_HEIGHT or ball01.getCenter().getY() - BALL_RAD <= 0 :
            gameOver = 1
        #If the pipe reaches the left side, winner
        if xPipe <= 0:
            winner = 1
        #If the ball's xcord (+- the radius of the ball) is within the pipe's range check the nested if
        if ball01.getCenter().getX() + BALL_RAD >= xPipe and ball01.getCenter().getX() - BALL_RAD <= xPipe + PIPE_WIDTH :
            #if the ball's ycord (+- the radius of the ball) is within the pipe's range, gameover
            if ball01.getCenter().getY() - BALL_RAD <= PIPE_LENGTH or ball01.getCenter().getY() + BALL_RAD >= WIN_HEIGHT-PIPE_LENGTH:
                gameOver = 1        
        #If gameover has been triggered, turn the ball red and break the loop
        if gameOver == 1 :
            ball01.setFill("red")
            break
        #If winner has been triggered, turn the ball green and break the loop
        if winner == 1:
            level = level +1
            break
        #Make the ball fall
        ball01.move(0, MOVEY)
        #Make both pipes move left
        topPipeList[level].move(-MOVEX, 0)
        bottomPipeList[level].move(-MOVEX, 0)
        #advance the counter that is equal the x cord of the leading edge of the pipe
        xPipe = xPipe - MOVEX
        #refresh the screen
        update(UPDATE_RATE)
