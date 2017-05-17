# flappyBall.py
# Clinton Peterson
# 16 May 2017

from graphics import *
import random

#Define Constants
WIN_WIDTH = 800   #Pixels
WIN_HEIGHT = 800  #Pixels
UPDATE_RATE = 60 #frames per second
BALL_RAD = 30 #ball Size in Pixels
MOVEX = 2 #pipe's moving left speed
MOVEY = 2 #falling speed
PIPE_LENGTH = 30\0 #in pixels, from floor and ceiling
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

#Setup the pipes
tRect01 = Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,0), Point(WIN_WIDTH,PIPE_LENGTH))
tRect01.setFill("blue")
tRect01.setOutline("black")
tRect01.draw(win)
bRect01 = Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,WIN_HEIGHT), Point(WIN_WIDTH,WIN_HEIGHT-PIPE_LENGTH))
bRect01.setFill("blue")
bRect01.setOutline("black")
bRect01.draw(win)

#setting variables to be changed when you win or lose
gameOver = 0
winner = 0

#This sets a variable to be the same as the x cord of the leading edge of the pipe
xPipe = WIN_WIDTH - PIPE_WIDTH

#Main Program
while True:
    key = win.checkKey()
    #for every space bar it flaps up 20 times what it falls each frame
    if key == "space":
        ball01.move(0, -20 * MOVEY)
    #if the ball hits the bottom, you lose
    if ball01.getCenter().getY() > WIN_HEIGHT - BALL_RAD :
        gameOver = 1
    #if the pipe reaches the left side, you win
    if xPipe <= 0:
        winner = 1
    #if the ball's xcord (+- the radius of the ball) is within the pipe's range check the nested if
    if ball01.getCenter().getX() + BALL_RAD >= xPipe and ball01.getCenter().getX() - BALL_RAD <= xPipe + PIPE_WIDTH :
        #if the ball's ycord (+- the radius of the ball) is within the pipe's range, game over
        if ball01.getCenter().getY() - BALL_RAD <= PIPE_LENGTH or ball01.getCenter().getY() + BALL_RAD >= WIN_HEIGHT-PIPE_LENGTH:
            gameOver = 1        
    #if gameover has been triggered, turn the ball red and break the loop
    if gameOver == 1 :
        ball01.setFill("red")
        break
    #if winner has been triggered, turn the ball 
    if winner == 1:
        ball01.setFill("green")
        break
    #make the ball fall
    ball01.move(0, MOVEY)
    #make both rectangles move left
    tRect01.move(-MOVEX, 0)
    bRect01.move(-MOVEX, 0)
    #advance the counter that is equal the x cord of the leading edge of the pipe
    xPipe = xPipe - MOVEX
    #refresh the screen
    update(UPDATE_RATE)
