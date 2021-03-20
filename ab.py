from graphics import *
win =GraphWin()
pt=Point(100,100)
pt.draw(win)
pt.setFill("blue")

cir=Circle(pt,25)
cir.draw(win)
cir.setOutline("red")
cir.setFill("yellow")

line=Line(pt,Point(80,90))
line.draw(win)
line.setFill("green")

rect=Rectangle(Point(150,150),pt)
rect.draw(win)
rect.setFill("pink")
win.getMouse()
win.closed()