# lander.py
# Clinton Peterson
# 23 May 2017

from graphics import *
import random

WIN_WIDTH = 800 #Pixels
WIN_HEIGHT = 800 #Pixels
UPDATE_RATE = 60 #frames per second
LANDER_SIZE = 30
GRAVITY = 0.05 
THRUST = 0.5

win = GraphWin("Lander", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("white")


lander01 = Circle(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), LANDER_SIZE)
lander01.setFill("black")
lander01.setOutline("blue")
lander01.draw(win)

fallingSpeed = 1

message1 = Text(Point(200,200), fallingSpeed)
message1.draw(win)


while True:    
    
    message1.setText(fallingSpeed)

    if lander01.getCenter().getY() + LANDER_SIZE >= WIN_HEIGHT or lander01.getCenter().getY() - LANDER_SIZE <= 0 :
        break
    key = win.checkKey()        
    if key == "space":
        fallingSpeed = fallingSpeed - THRUST
    fallingSpeed = fallingSpeed + GRAVITY
    lander01.move(0, fallingSpeed)        
    update(UPDATE_RATE)
