#requires graphics.py, written by John Zelle for use with the book "Python Programming: 
#An Introduction to Computer Science" (Franklin, Beedle & Associates).
from graphics import *

win = GraphWin()

point1 = Point(20, 30)
point2 = Point(27, 8)
point1.draw(win)
point2.draw(win)
print("Point 1 is at x=", point1.getX(), "y=", point1.getY())

center = Point(99.5, 99.5)
circle = Circle(center, 30)
circle.setFill('Green')
circle.draw(win)

top_left = Point(12, 12)
bottom_right = Point(36, 36)
rectangle = Rectangle(top_left,bottom_right)
rectangle.setFill('Purple')
rectangle.draw(win)

point_a = Point(75, 5)
point_b = Point(175, 180)
line = Line(point_a, point_b)
line.draw(win)

oval = Oval(Point(93, 102), Point(32, 67))
oval.setFill('Blue')
oval.draw(win)

text = Text(Point(99.5, 150), "Howdy, Folks")
text.draw(win)

input("press enter close. ")

win.close()
