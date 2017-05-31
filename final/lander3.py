# lander.py
# Clinton Peterson
# 23 May 2017

from graphics import *
import random

WIN_WIDTH = 800 #Pixels
WIN_HEIGHT = 800 #Pixels
UPDATE_RATE = 60 #frames per second
GRAVITY = 0.01 
THRUST = 1
FUEL = 100 

win = GraphWin("Lander", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("white")

lander01 = Image(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), "lander.gif")
lander01.draw(win)

def landerReset():
    global lander01
    lander01.undraw()
    lander01 = Image(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), "lander.gif")
    lander01.draw(win)

#Initial rate of decent
fallingSpeed = 0
#Initial rate of lateral movement
lateralSpeed = 0
verticalDisplay =  str(round(10*fallingSpeed,2))

message1 = Text(Point(50,100), verticalDisplay)
message1.draw(win)
message2 = Text(Point(50,130), lateralSpeed)
message2.draw(win)
message3 = Text(Point(50,160), FUEL)
message3.draw(win)
message4 = Text(Point(150,100), "Rate of decent")
message4.draw(win)
message5 = Text(Point(150,130), "    Lateral speed")
message5.draw(win)
message6 = Text(Point(150,160), "    Fuel remaining")
message6.draw(win)

playAgain = 1
while playAgain == 1:
    

    #Initial rate of decent
    fallingSpeed = 0
    #Initial rate of lateral movement
    lateralSpeed = 0

    
    landingPadList = []
    for i in range(WIN_WIDTH//100):
        landingPadList.append(Line(Point(i*100,WIN_HEIGHT), Point(i*100+100,WIN_HEIGHT)))
        landingPadList[i].setOutline("#%06x" % random.randint(0, 0xFFFFFF))
        landingPadList[i].setFill("#%06x" % random.randint(0, 0xFFFFFF))
        landingPadList[i].setWidth(20)
        landingPadList[i].draw(win)





    while True:    
        verticalDisplay =  str(round(10*fallingSpeed,2))
        message1.setText(verticalDisplay)
        message2.setText(lateralSpeed)
        message3.setText(FUEL)
        topEdge = lander01.getAnchor().getY() - lander01.getHeight()/2 
        bottomEdge = lander01.getAnchor().getY() + lander01.getHeight()/2
        leftEdge = lander01.getAnchor().getX() - lander01.getWidth()/2 
        rightEdge = lander01.getAnchor().getX() + lander01.getWidth()/2
        if bottomEdge >= WIN_HEIGHT - 10 or topEdge <= 0 or leftEdge <= 0 or rightEdge >= WIN_WIDTH :
            break
        key = win.checkKey()        
        if key == "space" and FUEL != 0:
            fallingSpeed = fallingSpeed - THRUST
            FUEL -= 1
        if key == "Left" and FUEL != 0:
            lateralSpeed = lateralSpeed - THRUST
            FUEL -= 1
        if key == "Right" and FUEL != 0:
            lateralSpeed = lateralSpeed + THRUST
            FUEL -= 1
        fallingSpeed = fallingSpeed + GRAVITY          
        lander01.move(lateralSpeed, fallingSpeed) 
        update(UPDATE_RATE)





    message7 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "GAME OVER")
    message7.draw(win)
    message8 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "Press y to play again or n to quit")
    message8.draw(win)
    update(UPDATE_RATE)

    while True:
        key = win.checkKey()
        if key == "y":
            message7.undraw()
            message8.undraw()
            for i in range(WIN_WIDTH//100):
                landingPadList[i].undraw()
            landerReset()
            break
        if key == "n":
            playAgain = 0
            break
