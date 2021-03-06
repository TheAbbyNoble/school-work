#requires graphics.py, written by John Zelle for use with the book "Python Programming: 
#An Introduction to Computer Science" (Franklin, Beedle & Associates).

from graphics import *

win = GraphWin("Draw a triangle")

win.setCoords(0.0, 0.0, 10.0, 10.0)

textMessage = Text(Point(5.0, 0.5), "Click thingy")
textMessage.draw(win)

point1 = win.getMouse()
point1.draw(win)

point2 = win.getMouse()
point2.draw(win)

point3 = win.getMouse()
point3.draw(win)

triangle = Polygon(point1, point2, point3)
triangle.setFill("peachpuff")
triangle.setOutline("cyan")
triangle.draw(win)

input("Press whatever")
