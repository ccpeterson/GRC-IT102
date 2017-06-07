# lander.py
# Clinton Peterson
# 23 May 2017

from graphics import *
import random

#constants for game setup
WIN_WIDTH = 800 #window width in pixels
WIN_HEIGHT = 800 #window height in pixels
UPDATE_RATE = 60 #Frames per second
PAD_WIDTH = 100 #width of each individual landing pad
GRAVITY = 0.01 #increase to downward velocity each frame 
THRUST = 1 #increase to upward or lateral velocity with each thrust
STARTING_FUEL = 30  #ammount of thrusts allowed per round

#function to reset the lander position after a round
def landerReset():
    global lander01
    lander01.undraw()
    lander01 = Image(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), "lander.gif")
    lander01.draw(win)

#setup the window
win = GraphWin("Lander", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("white")

#display instructions and wait for a space bar to start the game
instructions1 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2-100), "Welcome to Lander. Your mission is to land on the color indicated in the top right corner.")
instructions1.draw(win)
instructions2 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2-50), "Left and right arrows control your lateral movement. Space bar fires your main thruster which slows your decent")
instructions2.draw(win)
instructions3 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "You must land with no lateral movement and a rate of decent less then 10")
instructions3.draw(win)
instructions4 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+50), "You will also crash if you hit the sides or top of the screen.")
instructions4.draw(win)
instructions5 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "Press the space bar to start the game.")
instructions5.draw(win)
while True:
        key = win.checkKey()
        if key == "space":
            instructions1.undraw()
            instructions2.undraw()
            instructions3.undraw()
            instructions4.undraw()
            instructions5.undraw()
            break
#draw the initial lander at the starting position
lander01 = Image(Point(WIN_WIDTH/2 ,WIN_HEIGHT/2), "lander.gif")
lander01.draw(win)
#setup of velocity and fuel varibales for initial display
fuel = STARTING_FUEL
fallingSpeed = 0
lateralSpeed = 0
#setup of varibale used for displaying decent rate
verticalDisplay =  str(round(10*fallingSpeed,2))
#setup of display
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
#main loop of game mechanic
playAgain = 1
while playAgain == 1:
    #reset variables each round
    fuel = STARTING_FUEL
    winner = 0
    loser = 0
    fallingSpeed = 0
    lateralSpeed = 0
    flameCounter = 0
    #create the landing pads and pick one randomly to be the target each round
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
    #display a rectangle in the top right that will be the same color as the target
    target01 = Rectangle(Point((WIN_WIDTH - 100),0), Point(WIN_WIDTH,100))
    target01.setFill(targetColor)
    target01.draw(win)
    #starting the loop that runs each frame
    while True:    
        #update all the displays
        verticalDisplay =  str(round(10*fallingSpeed,2))
        message1.setText(verticalDisplay)
        message3.setText(lateralSpeed)
        message5.setText(fuel)
        #set variables that are equal to the current position of the landers edges
        topEdge = lander01.getAnchor().getY() - lander01.getHeight()/2 
        bottomEdge = lander01.getAnchor().getY() + lander01.getHeight()/2
        leftEdge = lander01.getAnchor().getX() - lander01.getWidth()/2 
        rightEdge = lander01.getAnchor().getX() + lander01.getWidth()/2
        #if the bottom edge touches the landing pad AND the center of the lander is above the correct target pad AND the rate of decent is slow enough AND it's not moving sideways then the win condition is met 
        if bottomEdge >= WIN_HEIGHT - 10 and lateralSpeed == 0 and fallingSpeed < 1 and lander01.getAnchor().getX() > (randomPad * PAD_WIDTH) and lander01.getAnchor().getX() < (randomPad * PAD_WIDTH + PAD_WIDTH):
            winner = 1
            break
        #if the and edge of the lander touches the edges then the lose condition is met
        if bottomEdge >= WIN_HEIGHT - 10 or topEdge <= 0 or leftEdge <= 0 or rightEdge >= WIN_WIDTH :
            loser = 1
            break        
        #checking for keyboard input each frame and applying thrust appropriately
        key = win.checkKey()        
        if key == "space" and fuel != 0:
            fallingSpeed = fallingSpeed - THRUST
            fuel -= 1
            try:
                flame
            except NameError:   
                noFlame =1
            else:
                flame.undraw()
            flame = Image(Point(lander01.getAnchor().getX() , bottomEdge +50), "thrustDown.gif")
            flame.draw(win)
            flameCounter = UPDATE_RATE //2
        if key == "Left" and fuel != 0:
            lateralSpeed = lateralSpeed - THRUST
            fuel -= 1
            try:
                flame
            except NameError:   
                noFlame =1
            else:
                flame.undraw()
            flame = Image(Point(rightEdge +50 , lander01.getAnchor().getY()), "thrustRight.gif")
            flame.draw(win)
            flameCounter = UPDATE_RATE //2
        if key == "Right" and fuel != 0:
            lateralSpeed = lateralSpeed + THRUST
            fuel -= 1
            try:
                flame
            except NameError:   
                noFlame =1
            else:
                flame.undraw()
            flame = Image(Point(leftEdge - 50 , lander01.getAnchor().getY()), "thrustLeft.gif")
            flame.draw(win)
            flameCounter = UPDATE_RATE //2
        #adding gravity to the current falling speed
        fallingSpeed = fallingSpeed + GRAVITY
        #moving the lander for every frame the current speed
        lander01.move(lateralSpeed, fallingSpeed) 
        
        flameCounter -= 1
        if flameCounter == 0:
            try:
                flame
            except NameError:   
                noFlame =1
            else:
                flame.undraw()
        if flameCounter > 0:
            try:
                flame
            except NameError:   
                noFlame =1
            else:
                flame.move(lateralSpeed, fallingSpeed)
        update(UPDATE_RATE)
    #remove the target rectangle
    target01.undraw()
    try:
        flame
    except NameError:   
        noFlame =1
    else:
        flame.undraw()
    if loser == 1:
        #remove the lander image and replace it with an explosion image
        lander01.undraw()
        lander01 = Image(Point(lander01.getAnchor().getX() ,lander01.getAnchor().getY()), "boom.gif")
        lander01.draw(win)
        #display the results
        popup1 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "YOU DIED IN THE COLD VACCUM OF SPACE, GAME OVER")
        popup1.draw(win)
        popup2 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "Press y to play again or n to quit")
        popup2.draw(win)
        update(UPDATE_RATE)
    if winner == 1:
        #display the results
        popup1 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "YOU WIN!")
        popup1.draw(win)
        popup2 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "Press y to play again or n to quit")
        popup2.draw(win)
        update(UPDATE_RATE)
        
    #wait for a y or n
    while True:
        key = win.checkKey()
        if key == "y":
            #undraw the popup display, the landing pads, and call 
            popup1.undraw()
            popup2.undraw()
            for i in range(WIN_WIDTH//100):
                landingPadList[i].undraw()
            landerReset()
            break
        if key == "n":
            playAgain = 0
            break
