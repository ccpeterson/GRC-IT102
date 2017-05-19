from graphics import*

win = GraphWin("Flappy Ball", 500, 500, autoflush=False)
win.setBackground("grey")
UPDATE_RATE = 60 #frames per second

while True:
    key = win.checkKey()
    message4 = Text(Point(250,250), key)
    message4.draw(win)
    update(UPDATE_RATE)
