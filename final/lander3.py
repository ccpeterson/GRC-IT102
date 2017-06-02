# lander.py
# Clinton Peterson
# 23 May 2017

from graphics import *
import random

WIN_WIDTH = 800 #Pixels
WIN_HEIGHT = 800 #Pixels
UPDATE_RATE = 60 #frames per second
PAD_WIDTH = 100
GRAVITY = 0.01 
THRUST = 1
STARTING_FUEL = 50 

def landerReset():
    global lander01
    lander01.undraw()
    lander01 = Image(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), "lander.gif")
    lander01.draw(win)

win = GraphWin("Lander", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("white")

instructions1 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2-100), "Welcome to Lander. Your mission is to land on the color indicated in the top right corner.")
instructions1.draw(win)
instructions2 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "Left and right arrows control your lateral movement. Space bar fires your main thruster which slows your decent")
instructions2.draw(win)
instructions3 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "You must land with no lateral movement and a rate of decent less then 10")
instructions3.draw(win)
while True:
        key = win.checkKey()
        if key == "space":
            instructions1.undraw()
            instructions2.undraw()
            instructions3.undraw()
            break

lander01 = Image(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), "lander.gif")
lander01.draw(win)
fuel = STARTING_FUEL
#Initial rate of decent
fallingSpeed = 0
#Initial rate of lateral movement
lateralSpeed = 0
verticalDisplay =  str(round(10*fallingSpeed,2))

message1 = Text(Point(50,100), verticalDisplay)
message1.draw(win)
message2 = Text(Point(150,100), "Rate of decent")
message2.draw(win)
message3 = Text(Point(50,130), lateralSpeed)
message3.draw(win)
message4 = Text(Point(150,130), "    Lateral speed")
message4.draw(win)
message5 = Text(Point(50,160), fuel)
message5.draw(win)
message6 = Text(Point(150,160), "    fuel remaining")
message6.draw(win)

playAgain = 1
while playAgain == 1:
    fuel = STARTING_FUEL
    winner = 0
    loser = 0
    fallingSpeed = 0
    lateralSpeed = 0
    
    landingPadList = []
    randomPad = random.randint(0, (WIN_WIDTH//PAD_WIDTH))
    for i in range(WIN_WIDTH//PAD_WIDTH):
        landingPadList.append(Line(Point(i*100,WIN_HEIGHT), Point(i*100+100,WIN_HEIGHT)))
        randomColor = "#%06x" % random.randint(0, 0xFFFFFF)
        landingPadList[i].setOutline(randomColor)
        landingPadList[i].setFill(randomColor)
        landingPadList[i].setWidth(20)
        landingPadList[i].draw(win)
        if i == randomPad:
            targetColor = randomColor

    target01 = Rectangle(Point((WIN_WIDTH - 100),0), Point(WIN_WIDTH,100))
    target01.setFill(targetColor)
    target01.draw(win)

    while True:    
        verticalDisplay =  str(round(10*fallingSpeed,2))
        message1.setText(verticalDisplay)
        message3.setText(lateralSpeed)
        message5.setText(fuel)
        topEdge = lander01.getAnchor().getY() - lander01.getHeight()/2 
        bottomEdge = lander01.getAnchor().getY() + lander01.getHeight()/2
        leftEdge = lander01.getAnchor().getX() - lander01.getWidth()/2 
        rightEdge = lander01.getAnchor().getX() + lander01.getWidth()/2
        if bottomEdge >= WIN_HEIGHT - 10 and lateralSpeed == 0 and fallingSpeed < 1 and lander01.getAnchor().getX() > (randomPad * PAD_WIDTH) and lander01.getAnchor().getX() < (randomPad * PAD_WIDTH + PAD_WIDTH):
            winner = 1
            break
        if bottomEdge >= WIN_HEIGHT - 10 or topEdge <= 0 or leftEdge <= 0 or rightEdge >= WIN_WIDTH :
            loser = 1
            break        
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
        lander01.move(lateralSpeed, fallingSpeed) 
        update(UPDATE_RATE)

    target01.undraw()
    xBoom = lander01.getAnchor().getX()
    yBoom = lander01.getAnchor().getY()
    if loser == 1:
        lander01.undraw()
        lander01 = Image(Point(xBoom ,yBoom), "boom.gif")
        lander01.draw(win)
        popup1 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "YOU DIED, GAME OVER")
        popup1.draw(win)
        popup2 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "Press y to play again or n to quit")
        popup2.draw(win)
        update(UPDATE_RATE)
    if winner == 1:
        popup1 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "YOU WIN!, GAME OVER")
        popup1.draw(win)
        popup2 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "Press y to play again or n to quit")
        popup2.draw(win)
        update(UPDATE_RATE)

    while True:
        key = win.checkKey()
        if key == "y":
            popup1.undraw()
            popup2.undraw()
            for i in range(WIN_WIDTH//100):
                landingPadList[i].undraw()
            landerReset()
            break
        if key == "n":
            playAgain = 0
            break
