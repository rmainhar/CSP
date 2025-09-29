#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

#Create custom turtle shape
trtl.addshape("diamond",((0,-6), (6,3), (5,5), (4,6), (-4,6), (-5,5), (-6,3)))

# create an empty list of turtles
my_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "diamond", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#Starting Position
startx = -75
starty = 25
new_angle = 90

#Making Turtles
for t in my_turtles:
  new_color = turtle_colors
  new_color = turtle_colors.pop()
  t.color(new_color)
  t.fillcolor(new_color)
  t.pencolor(new_color)
  t.pensize(5)
  t.setheading(new_angle)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(30)
  new_angle = t.heading()
  t.forward(50)

#Setting New Starting Position
  '''startx = startx + 50
  starty = starty + 50'''
  startx = t.xcor()
  starty = t.ycor()
  
wn = trtl.Screen()
wn.mainloop()