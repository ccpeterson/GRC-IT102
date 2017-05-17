# flappyBall.py
# Clinton Peterson
# 16 May 2017

from graphics import *
import random

#Define Constants
WIN_WIDTH = 800   #Pixels
WIN_HEIGHT = 800  #Pixels
UPDATE_RATE = 60 #Frames per second
BALL_RAD = 20 #Ball Size in Pixels
MOVEX = 1 #moving left speed
MOVEY = 2 #falling speed
PIPE_LENGTH = 300
PIPE_WIDTH = 50


#Setup graphics window object
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")

#Setup up the ball and pipes
ball01 = Circle(Point(100 ,WIN_HEIGHT/2), BALL_RAD)
ball01.setFill("blue")
ball01.setOutline("black")
ball01.setWidth(5)
ball01.draw(win)

tRect01 = Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,0), Point(WIN_WIDTH,PIPE_LENGTH))
tRect01.setFill("blue")
tRect01.setOutline("black")
tRect01.draw(win)
bRect01 = Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,WIN_HEIGHT), Point(WIN_WIDTH,WIN_HEIGHT-PIPE_LENGTH))
bRect01.setFill("blue")
bRect01.setOutline("black")
bRect01.draw(win)

gameOver = 0
winner = 0
xPipe = WIN_WIDTH - PIPE_WIDTH
#Main Program
while True:
    key = win.checkKey()
    if key == "space":
        ball01.move(0, -20 * MOVEY)
    if ball01.getCenter().getY() > WIN_HEIGHT - BALL_RAD :
        gameOver = 1
    if xPipe == 0:
        winner = 1
    if ball01.getCenter().getX() >= xPipe :
        if ball01.getCenter().getY()  < PIPE_LENGTH or ball01.getCenter().getY()   > WIN_HEIGHT-PIPE_LENGTH :
            gameOver = 1        
    if gameOver == 1 :
        ball01.setFill("red")
        break
    if winner == 1:
        ball01.setFill("green")
        break
    
    ball01.move(0, MOVEY)
    tRect01.move(-MOVEX, 0)
    bRect01.move(-MOVEX, 0)
    xPipe = xPipe - MOVEX
    update(UPDATE_RATE)




