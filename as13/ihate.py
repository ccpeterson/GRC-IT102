from graphics import *
import random

WIN_WIDTH = 800 #Pixels
WIN_HEIGHT = 800 #Pixels
UPDATE_RATE = 60 #frames per second
BALL_RAD = 30 #ball Size in Pixels
MOVEX = 2 #Pipe's moving left speed
MOVEY = 2 #Falling speed in pixels per frame
GAP_HEIGHT = 250 #in pixels
PIPE_WIDTH = 50 #in pixels

win = GraphWin("Flappy Ball", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")


ball01 = Circle(Point(200 ,WIN_HEIGHT/2), BALL_RAD)
ball01.setFill("blue")
ball01.setOutline("black")
ball01.setWidth(5)
ball01.draw(win)

def ballReset():
    global ball01
    ball01.undraw()
    ball01 = Circle(Point(200 ,WIN_HEIGHT/2), BALL_RAD)
    ball01.setFill("blue")
    ball01.setOutline("black")
    ball01.setWidth(5)
    ball01.draw(win)

topPipeList = []
bottomPipeList = []
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

wall=0
level = 0
message1 = Text(Point(WIN_WIDTH//2,100), "-Spacebar to flap-")
message1.draw(win)
message2 = Text(Point(WIN_WIDTH//2,150), "-q to quit-")
message2.draw(win)
message3 = Text(Point(WIN_WIDTH//2,200), "-Pipes passed-")
message3.draw(win)
message4 = Text(Point(WIN_WIDTH//2,240), level)
message4.draw(win)


playAgain = 1
while playAgain == 1:
    gameOver = 0
    level = 0
    message4.setText(level)
    while True:
        if gameOver == 1:
            topPipeList[level].undraw()
            bottomPipeList[level].undraw()
            ball01.setFill("red")
            break 
        makePipes(wall)
        
        xPipe = WIN_WIDTH - PIPE_WIDTH
        winner = 0
        while True:    
            key = win.checkKey()        
            if key == "space":
                ball01.move(0, -20 * MOVEY)        
            if key == "q":
                gameOver = 1        
            if ball01.getCenter().getY() + BALL_RAD >= WIN_HEIGHT or ball01.getCenter().getY() - BALL_RAD <= 0 :
                gameOver = 1        
            if xPipe < -PIPE_WIDTH:
                winner = 1                            
            #If the ball's xcord (+- the radius of the ball) is within the pipe's range check the nested if
            if ball01.getCenter().getX() + BALL_RAD >= xPipe and ball01.getCenter().getX() - BALL_RAD <= xPipe + PIPE_WIDTH :
                #if the ball's ycord (+- the radius of the ball) is within the pipe's range, gameover
                if ball01.getCenter().getY() - BALL_RAD <= topPipeHeight or ball01.getCenter().getY() + BALL_RAD >= topPipeHeight + GAP_HEIGHT:
                    gameOver = 1       
            if gameOver == 1 :
                topPipeList[wall].undraw()
                bottomPipeList[wall].undraw()
                ball01.setFill("red")
                break        
            if winner == 1:
                topPipeList[wall].undraw()
                bottomPipeList[wall].undraw()
                level = level +1
                message4.setText(level)                
                break        
            ball01.move(0, MOVEY)        
            topPipeList[wall].move(-MOVEX, 0)
            bottomPipeList[wall].move(-MOVEX, 0)        
            xPipe = xPipe - MOVEX        
            update(UPDATE_RATE)
        wall = wall + 1
            
            
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
            ballReset()
            break
        if key == "n":
            playAgain = 0
            break
