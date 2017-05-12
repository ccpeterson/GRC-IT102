#Graphics stuff
#11 May 17

from graphics import *

from graphics import *
win = GraphWin("My Circle", 100, 100)
circle01 = Circle(Point(50,50), 10)
circle01.draw(win)
win.getMouse() # Pause to view result
win.close() # Close the graphics window

