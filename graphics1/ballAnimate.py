# ballAnimate.py
# Ball bounce using graphics.py library
# Rich Bankhead
# 23 January 2017


from graphics import *
import time

#Define Constants
WIN_WIDTH = 800   #Pixels
WIN_HEIGHT = 800  #Pixels
UPDATE_RATE = 60 #Frames per second
BALL_RAD = 50


#Setup graphics window object
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT)
win.autoflush = False
win.setBackground("blue")

#Setup up the ball
ball01 = Circle(Point(WIN_WIDTH/2,WIN_HEIGHT/2), BALL_RAD)
ball01.setFill("red")
ball01.setOutline("black")
ball01.setWidth(5)
ball01.draw(win)

moveX = 20
moveY = 20

def up():
    ball01.move(0, -moveY)

def down():
    ball01.move(0, +moveY)

def right():
    ball01.move(moveX, 0)

def left():
    ball01.move(-moveX, 0)


####### Main Program

while True:
    key = win.checkKey()
    
    if key == "Up":
        up()
    elif key == "Down":
        down()
    elif key == "Right":
        right()
    elif key == "Left":
        left()
    elif key == "space":
        break
    update(UPDATE_RATE)
    
win.close()
  

