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

ball03 = Circle(Point(random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD)),random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD))), BALL_RAD )
ball03.setFill("green")
ball03.setOutline("black")
ball03.setWidth(5)
ball03.draw(win)

ball04 = Circle(Point(random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD)),random.randint(BALL_RAD,(WIN_HEIGHT - BALL_RAD))), BALL_RAD)
ball04.setFill("yellow")
ball04.setOutline("black")
ball04.setWidth(5)
ball04.draw(win)

moveX = 5
moveY = 5

xDir1 = 1
yDir1 = 1
xDir2 = 1
yDir2 = 1
xDir3 = 1
yDir3 = 1
xDir4 = 1
yDir4 = 1

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
    if ball03.getCenter().getX() > WIN_WIDTH-BALL_RAD or ball03.getCenter().getX() < BALL_RAD:
        xDir3 *= -1        
        ball03.setFill("#%06x" % random.randint(0, 0xFFFFFF))
    if ball03.getCenter().getY() > WIN_WIDTH-BALL_RAD or ball03.getCenter().getY() < BALL_RAD:
        yDir3 *= -1
        ball03.setFill("#%06x" % random.randint(0, 0xFFFFFF))
    if ball04.getCenter().getX() > WIN_WIDTH-BALL_RAD or ball04.getCenter().getX() < BALL_RAD:
        xDir4 *= -1        
        ball04.setFill("#%06x" % random.randint(0, 0xFFFFFF))
    if ball04.getCenter().getY() > WIN_WIDTH-BALL_RAD or ball04.getCenter().getY() < BALL_RAD:
        yDir4 *= -1        
        ball04.setFill("#%06x" % random.randint(0, 0xFFFFFF))
    ball01.move(moveX*xDir1, moveY*yDir1)
    ball02.move(moveX*xDir2, moveY*yDir2)
    ball03.move(moveX*xDir3, moveY*yDir3)
    ball04.move(moveX*xDir4, moveY*yDir4)
    update(UPDATE_RATE)


