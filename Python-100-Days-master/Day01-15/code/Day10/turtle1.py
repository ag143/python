"""

Drawing with turtle module
This is a very interesting module that simulates a turtle crawling on a window to draw

Version: 0.1
Author: author
Date: 2018-03-14

"""

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for_in range(36):
     turtle.forward(200)
     turtle.right(170)
turtle.end_fill()
turtle.mainloop()