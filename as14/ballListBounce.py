# ballListBouce.py
# Clinton Peterson
# 25 May 2017

from graphics import *
import random

WIN_WIDTH = 800 #Pixels
WIN_HEIGHT = 800 #Pixels
UPDATE_RATE = 60 #frames per second
BALL_SIZE = 30 #ball Size in Pixels
BALL_OUTLINE = 2 #width of ball border in pixels
NUM_BALLS = 10 #how many balls

#Setup graphics window object
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")

#Create the lists
ballList = []
xDirList=[]
yDirList=[]

#crate the balls
for i in range(NUM_BALLS):
    while True:
        xPosInit = random.randint(BALL_SIZE, WIN_WIDTH - BALL_SIZE)
        yPosInit = random.randint(BALL_SIZE, WIN_WIDTH - BALL_SIZE)
        #this checks that the newly created position isn't inside another already created ball
        samePos = 0
        for j in range(0,i-1):
            if abs(ballList[j].getCenter().getX() - xPosInit) <= 2*BALL_SIZE and abs(ballList[j].getCenter().getY() - yPosInit <= 2*BALL_SIZE):
                samePos += 1        
        if samePos == 0:
            break    
    #create a new ball in the list using the validated postion   
    ballList.append(Circle(Point(xPosInit,yPosInit), BALL_SIZE))
    ballList[i].setFill("#%06x" % random.randint(0, 0xFFFFFF))
    ballList[i].setWidth(BALL_OUTLINE)
    ballList[i].draw(win)
    #create a variable magnitude of x and y direction for each ball
    xDirInit = random.randint(-5,5)
    xDirList.append(xDirInit)
    yDirInit = random.randint(-5,5)
    yDirList.append(yDirInit)

while True:
    for i in range(NUM_BALLS):        
        if ballList[i].getCenter().getX() >= WIN_WIDTH-BALL_SIZE or ballList[i].getCenter().getX() <= BALL_SIZE:
            xDirList[i] *= -1        
            ballList[i].setFill("#%06x" % random.randint(0, 0xFFFFFF))        
        if ballList[i].getCenter().getY() >= WIN_HEIGHT-BALL_SIZE or ballList[i].getCenter().getY() <= BALL_SIZE:
            yDirList[i] *= -1        
            ballList[i].setFill("#%06x" % random.randint(0, 0xFFFFFF))
        for j in range (0,NUM_BALLS):
            if abs(ballList[i].getCenter().getX() - ballList[j].getCenter().getX()) <= 2*BALL_SIZE and abs(ballList[i].getCenter().getY() - ballList[j].getCenter().getY()) <= 2*BALL_SIZE and j > i:
                xDirList[i] , yDirList[i] = -yDirList[i] , xDirList[i]
                xDirList[j] , yDirList[j] = -yDirList[j] , xDirList[j]
                ballList[i].move(2*xDirList[i], 2*yDirList[i])
                ballList[j].move(2*xDirList[j], 2*yDirList[j])        
        ballList[i].move(xDirList[i], yDirList[i])
    update(UPDATE_RATE)
