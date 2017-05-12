# graphicsdemo.py
# Graphics Demo
# Rich Bankhead
# 02 March 2017


from graphics import *
import random

#Define Constants
WIN_WIDTH = 800   #Pixels
WIN_HEIGHT = 800  #Pixels
UPDATE_RATE = 60 #Frames per second
BALL_RAD = 50


#Setup graphics window object
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")

#Setup up the balls

ball01 = Circle(Point(random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD)),random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD))), BALL_RAD  )
ball01.setFill("red")
ball01.setOutline("black")
ball01.setWidth(5)
ball01.draw(win)

ball02 = Circle(Point(random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD)),random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD))), BALL_RAD )
ball02.setFill("blue")
ball02.setOutline("black")
ball02.setWidth(5)
ball02.draw(win)



moveX = 5
moveY = 5

xDir1 = 1
yDir1 = 1
xDir2 = 1
yDir2 = 1


#Main Program
while True:
    if ball01.getCenter().getX() > WIN_WIDTH-BALL_RAD or ball01.getCenter().getX() < BALL_RAD:
        xDir1 *= -1        
        ball01.setFill("#%06x" % random.randint(0, 0xFFFFFF))        
    if ball01.getCenter().getY() > WIN_WIDTH-BALL_RAD or ball01.getCenter().getY() < BALL_RAD:
        yDir1 *= -1        
        ball01.setFill("#%06x" % random.randint(0, 0xFFFFFF))
    if ball02.getCenter().getX() > WIN_WIDTH-BALL_RAD or ball02.getCenter().getX() < BALL_RAD:
        xDir2 *= -1        
        ball02.setFill("#%06x" % random.randint(0, 0xFFFFFF))
    if ball02.getCenter().getY() > WIN_WIDTH-BALL_RAD or ball02.getCenter().getY() < BALL_RAD:
        yDir2 *= -1        
        ball02.setFill("#%06x" % random.randint(0, 0xFFFFFF))

    if abs(ball01.getCenter().getX() - ball02.getCenter().getX()) < 2*BALL_RAD and abs(ball01.getCenter().getY() - ball02.getCenter().getY()) < 2*BALL_RAD:
        xDir1 *= -1
        xDir2 *= -1
        yDir1 *= -1
        yDir2 *= -1
        ball01.setFill("#%06x" % random.randint(0, 0xFFFFFF))
        ball02.setFill("#%06x" % random.randint(0, 0xFFFFFF))
    
    ball01.move(moveX*xDir1, moveY*yDir1)
    ball02.move(moveX*xDir2, moveY*yDir2)
    
    update(UPDATE_RATE)


