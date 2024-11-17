# Draw a turtle bro!

import turtle
turtle.color('green')
for steps in range(2):
 turtle.forward(100)
 turtle.right(45)
turtle.color('red')
for steps in range(2):
 turtle.forward(100)
 turtle.right(45)
turtle.color('blue')
for steps in range(2):
 turtle.forward(100)
 turtle.right(45)
turtle.color('yellow')
for steps in range(2):
 turtle.forward(100)
 turtle.right(45)

nbrsides = 10
turtle.color('black')
for steps in range(nbrsides):
 turtle.forward(80)
 turtle.right(360/nbrsides)
 for steps in range(nbrsides):
  turtle.forward(20)
  turtle.right(360/nbrsides)

# # Save the drawing as a PostScript file 
# # (.ps files can be converted into jpg-png images easily! Just search the title of the file in your computer to find the file!)
# # cntrl+Κ+C add #, cntrl+Κ+U delete #!!!
# ts = turtle.getcanvas()
# ts.postscript(file="turtle_drawing.ps")
turtle.done()