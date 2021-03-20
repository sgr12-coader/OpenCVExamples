from graphics import *
def main():
    win=GraphWin("Face",200,150)
    head=Circle(Point(40,100),25)
    head.setFill("yellow")
    head.draw(win)

    eye1=Circle(Point(30,105),5)
    eye1.setFill("blue")
    eye1.draw(win)

    eye2=Line(Point(45,105),Point(55,105))
    eye2.setWidth(3)
    eye2.draw(win)

    mouse=Oval(Point(30,90),Point(50,85))
    mouse.setFill("red")
    mouse.draw(win)
6
    label=Text(Point(100,120),"A face")
    label.draw(win)

    message=Text(Point(win.getWidth()/2,20),"Click to quit")
    message.draw(win)
    win.getMouse()
    win.close()

main()