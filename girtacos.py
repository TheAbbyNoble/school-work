from graphics import *

win = GraphWin()

center = Point(99.5, 99.5)
circle = Circle(center, 60)
circle.setFill('Green')
circle.draw(win)

top_left = Point(75, 130)
bottom_right = Point(130, 136)
rectangle = Rectangle(top_left,bottom_right)
rectangle.setFill('Purple')
rectangle.draw(win)


point_a = Point(75,130)
point_b = Point(140, 130)
line = Line(point_a, point_b)
line.draw(win)

oval = Oval(Point(63, 72), Point(99, 99))
oval.setFill('Blue')
oval.draw(win)

oval = Oval(Point(113, 72), Point(140, 99))
oval.setFill('Blue')
oval.draw(win)

text = Text(Point(100.5, 180), "TACOS!!!!")
text.draw(win)

input("press enter close. ")

win.close()
