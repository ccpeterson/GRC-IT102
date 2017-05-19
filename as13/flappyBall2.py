# flappyBall2.py
# Clinton Peterson
# 18 May 2017

from graphics import *
import random

#Define Constants
WIN_WIDTH = 800 #Pixels
WIN_HEIGHT = 800 #Pixels
UPDATE_RATE = 60 #frames per second
BALL_RAD = 30 #ball Size in Pixels
MOVEX = 2 #Pipe's moving left speed
MOVEY = 2 #Falling speed in pixels per frame
GAP_HEIGHT = 250 #in pixels
PIPE_WIDTH = 50 #in pixels

#Setup graphics window object
win = GraphWin("Flappy Ball", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")

#Setup up the ball
def makeBall():
    global ball01
    ball01 = Circle(Point(200 ,WIN_HEIGHT/2), BALL_RAD)
    ball01.setFill("blue")
    ball01.setOutline("black")
    ball01.setWidth(5)
    ball01.draw(win)

#Setup the pipe lists
topPipeList = []
bottomPipeList = []

#Setup the pipe function
def makePipes(lvl):
    global topPipeHeight
    topPipeHeight = random.randint(100,WIN_HEIGHT - GAP_HEIGHT - 100)
    topPipeList.append(Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,0), Point(WIN_WIDTH,topPipeHeight)))
    topPipeList[lvl].setFill("green")
    topPipeList[lvl].setOutline("black")
    topPipeList[lvl].draw(win)
    bottomPipeList.append(Rectangle(Point(WIN_WIDTH-PIPE_WIDTH,WIN_HEIGHT), Point(WIN_WIDTH,topPipeHeight + GAP_HEIGHT)))
    bottomPipeList[lvl].setFill("green")
    bottomPipeList[lvl].setOutline("black")
    bottomPipeList[lvl].draw(win)
    

#Setup variable to be changed when you lose or win a level
gameOver = 0
level = 0

#Setup the text on the screen
message1 = Text(Point(WIN_WIDTH//2,100), "-Spacebar to flap-")
message1.draw(win)
message2 = Text(Point(WIN_WIDTH//2,150), "-q to quit-")
message2.draw(win)
message3 = Text(Point(WIN_WIDTH//2,200), "-Pipes passed-")
message3.draw(win)
message4 = Text(Point(WIN_WIDTH//2,240), level)
message4.draw(win)


#Main Program Loop
playAgain = 1
while playAgain == 1:
    makeBall()
    #Setup variable to be changed when you lose or win a level
    gameOver = 0
    level = 0
    while True:
        #if level loop was broken becuase you lost, stop
        if gameOver == 1:
            break
        #Draw the pipes
        makePipes(level)
        #Sets a variable to be the same as the x cord of the leading edge of the pipe
        xPipe = WIN_WIDTH - PIPE_WIDTH
        #resets the level win condition counter
        winner = 0
        #This loops during each level until you win or lose
        while True:
            #Setting a variable for key presses
            key = win.checkKey()
            #For every space bar it flaps up 20 times what it falls each frame
            if key == "space":
                ball01.move(0, -20 * MOVEY)
            #quiting
            if key == "q":
                gameOver = 1
            #If the ball hits the top bottom, gameover
            if ball01.getCenter().getY() + BALL_RAD >= WIN_HEIGHT or ball01.getCenter().getY() - BALL_RAD <= 0 :
                gameOver = 1
            #If the pipe reaches past the left side, you win the level
            if xPipe < -PIPE_WIDTH:
                winner = 1                            
            #If the ball's xcord (+- the radius of the ball) is within the pipe's range check the nested if
            if ball01.getCenter().getX() + BALL_RAD >= xPipe and ball01.getCenter().getX() - BALL_RAD <= xPipe + PIPE_WIDTH :
                #if the ball's ycord (+- the radius of the ball) is within the pipe's range, gameover
                if ball01.getCenter().getY() - BALL_RAD <= topPipeHeight or ball01.getCenter().getY() + BALL_RAD >= topPipeHeight + GAP_HEIGHT:
                    gameOver = 1        
            #If gameover has been triggered, turn the ball red and break the loop
            if gameOver == 1 :
                ball01.setFill("red")
                
                break
            #If winner has been triggered, iterate the level counter, updates the display and breaks the loop
            if winner == 1:
                topPipeList[level].undraw()
                bottomPipeList[level].undraw()
                level = level +1
                message4.setText(level)                
                break
            #Make the ball fall
            ball01.move(0, MOVEY)
            #Make both pipes move left
            topPipeList[level].move(-MOVEX, 0)
            bottomPipeList[level].move(-MOVEX, 0)
            #advance the counter that is equal the x cord of the leading edge of the pipe
            xPipe = xPipe - MOVEX
            #refresh the screen
            update(UPDATE_RATE)
    #A loop that waits for a command to restart or quit
    message5 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2), "GAME OVER")
    message5.draw(win)
    message6 = Text(Point(WIN_WIDTH//2,WIN_HEIGHT//2+100), "Press y to play again or n to quit")
    message6.draw(win)
    update(UPDATE_RATE)
    while True:
        key = win.checkKey()
        if key == "y":
            message5.undraw()
            message6.undraw()
            ball01.undraw()
            topPipeList[level].undraw()
            bottomPipeList[level].undraw()
            
            break
        if key == "n":
            playAgain = 0
            break
