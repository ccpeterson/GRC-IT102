# lander.py
# Clinton Peterson
# 23 May 2017

from graphics import *
import random

WIN_WIDTH = 800 #Pixels
WIN_HEIGHT = 800 #Pixels
UPDATE_RATE = 60 #frames per second
LANDER_SIZE = 30
GRAVITY = 0.01 
THRUST = 1
fuel = 100

win = GraphWin("Lander", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("white")


lander01 = Circle(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), LANDER_SIZE)
lander01.setFill("black")
lander01.setOutline("blue")
#lander01.draw(win)

lander02 = Image(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), "lander.gif")
lander02.draw(win)

fallingSpeed = 1
lateralSpeed = 0
fuel = 100

verticalDisplay =  str(round(10*fallingSpeed,2))

message1 = Text(Point(200,200), verticalDisplay)
message1.draw(win)
message2 = Text(Point(200,250), lateralSpeed)
message2.draw(win)
message3 = Text(Point(200,350), fuel)
message3.draw(win)

groundList = []
for i in range(WIN_WIDTH//100):
    
    groundList.append(Line(Point(i*100,WIN_HEIGHT-100), Point(i*100+100,WIN_HEIGHT-100)))
    groundList[i].setOutline("#%06x" % random.randint(0, 0xFFFFFF))
    groundList[i].setFill("#%06x" % random.randint(0, 0xFFFFFF))

    groundList[i].setWidth(10)
    groundList[i].draw(win)

while True:    
    verticalDisplay =  str(round(10*fallingSpeed,2))
    message1.setText(verticalDisplay)
    message2.setText(lateralSpeed)
    message3.setText(fuel)
    #if lander01.getCenter().getY() + LANDER_SIZE >= WIN_HEIGHT or lander01.getCenter().getY() - LANDER_SIZE <= 0 :
        #break
    key = win.checkKey()        
    if key == "space" and fuel != 0:
        fallingSpeed = fallingSpeed - THRUST
        fuel -= 1
    if key == "Left" and fuel != 0:
        lateralSpeed = lateralSpeed - THRUST
        fuel -= 1
    if key == "Right" and fuel != 0:
        lateralSpeed = lateralSpeed + THRUST
        fuel -= 1
    fallingSpeed = fallingSpeed + GRAVITY
    #lander01.move(lateralSpeed, fallingSpeed)        
    lander02.move(lateralSpeed, fallingSpeed) 
    update(UPDATE_RATE)
