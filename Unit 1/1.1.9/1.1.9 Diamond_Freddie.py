import turtle as trtl
#Create turtle shape
trtl.addshape("diamond",((0,-6), (6,3), (5,5), (4,6), (-4,6), (-5,5), (-6,3)))

#Lists
turtle_shape = ["diamond"]
start_position_x = [0,200,100,0,-166.6,0,-100,0,0,0]
start_position_y = [-200,100,100,166.6,166.6,-200,100,166.6,-200,0]
turtle_color = ["#b4e2ff", "#92d5ff", "#49b9ff", "#87CEFA", "#58bfff", "#78cbff", "#2dafff", "#11a4ff", "#009dff", "#38b3ff", "#a4dcff", "#73c9ff", "#22aaff"]
shape_position_x = [200,-100,166.6,-166.6,166.6,0,100,-66.6,-100,133.3,100,0,66.6] #last num in line is to not have error when popping
shape_position_y = [100, 166.6,200,200,100,166.6,200] #last num in list is to not have error when popping

#Variables
start_x = 0
start_y = -200
shapeX = int(shape_position_x[0])
shapeY = int(shape_position_y[0])

#Definitions
def start():
  t.penup()
  t.goto(start_x, start_y)
  t.pendown()

def begin():
  start_x = int(start_position_x[0])
  start_y = int(start_position_y[0])
  start()
  '''start_position_x.pop(0)
  start_position_y.pop(0)'''

def nextPos():
  global start_x
  global start_y
  start_position_x.pop(0)
  start_position_y.pop(0)
  start_x = int(start_position_x[0])
  start_y = int(start_position_y[0])


#Use color and size variations to enhance your artwork.
#Use these computational skills
    #Use iteration (looping) and conditional execution (if statements) to control the drawing.
    #Use a list that will have an affect on your artwork
    #Have user interaction have an affect on your artwork
    #Create a custom method(python def) that will be used in more than 1 location in your program 

#Choose descriptive variable names.
#Comment code segments or blocks of statements.

#Setting everything up
for s in turtle_shape:
  t = trtl.Turtle(shape=s)#Called it t to save time
  t.color("light sky blue")
  t.pencolor("black")
t.pensize(5)

#Going to where the drawing starts
begin()

#Shapes 1 and 2
for i in range (2):
  t.fillcolor(turtle_color[0])
  t.begin_fill()
  t.goto(shapeX, shapeY)
  t.back(100)
  shapeX = shape_position_x.pop(0)
  shapeX = int(shape_position_x[0])

  t.goto(start_x, start_y)
  t.end_fill()
  turtle_color.pop(0)
shapeY = shape_position_y.pop(0)
shapeY = int(shape_position_y[0])
nextPos()

#Shape 4 and 5
begin()

for i in range(2):
  t.fillcolor(turtle_color[0])
  t.begin_fill()
  t.back(100)
  t.goto(shapeX, shapeY)
  t.goto(start_x, start_y)
  t.end_fill()
  start_x = -1*start_y
  start_y = -1*start_x
  t.penup()
  t.goto(start_x, start_y)
  t.pendown()
  shapeX = shape_position_x.pop(0)
  shapeX = int(shape_position_x[0])
  turtle_color.pop(0)
nextPos()

#Shape 7 and 8
begin()

for i in range(2):
  t.fillcolor(turtle_color[0])
  t.begin_fill()
  t.goto(shapeX, shapeY)
  t.back(166.6)
  shapeX = shape_position_x.pop(0)
  shapeX = int(shape_position_x[0])
  t.goto(start_x, start_y)
  t.end_fill()
  start_x = -1*start_x
  start()
  turtle_color.pop(0)

shapeY = shape_position_y.pop(0)
shapeY = int(shape_position_y[0])
nextPos()

#Shape 9 and 10
begin()

for i in range(2):
  t.fillcolor(turtle_color[0])
  t.pendown()
  t.begin_fill()
  t.forward(166.6)
  t.goto(shapeX, shapeY)
  t.back(33.3)
  t.goto(start_x, start_y)
  t.end_fill()
  shapeX = shape_position_x.pop(0)
  shapeX = int(shape_position_x[0])
  turtle_color.pop(0)
  start_x = -166.6
  t.penup()
  t.goto(start_x, start_y)

shapeY = shape_position_y.pop(0)
shapeY = int(shape_position_y[0])
nextPos()

#Shape 11 and 12
begin()

for i in range(2):
  t.pendown()
  t.fillcolor(turtle_color[0])
  t.begin_fill()
  t.goto(shapeX, shapeY)
  t.back(33.3)
  t.goto(start_x, start_y)
  t.end_fill()
  shapeX = shape_position_x.pop(0)
  shapeX = int(shape_position_x[0])
  turtle_color.pop(0)
  start_x = 166.6
  t.penup()
  t.goto(start_x, start_y)

shapeY = shape_position_y.pop(0)
shapeY = int(shape_position_y[0])
nextPos()

#Shape 3
begin()

t.begin_fill()
t.fillcolor(turtle_color[0])
t.goto(shapeX, shapeY)
t.back(200)
t.goto(start_x, start_y)
turtle_color.pop(0)
t.end_fill()

shapeX = shape_position_x.pop(0)
shapeX = int(shape_position_x[0])
shapeY = shape_position_y.pop(0)
shapeY = int(shape_position_y[0])
nextPos()

#Shape 6
begin()

t.begin_fill()
t.fillcolor(turtle_color[0])
t.forward(200)
t.goto(shapeX, shapeY)
t.goto(start_x, start_y)
turtle_color.pop(0)
t.end_fill()

shapeX = shape_position_x.pop(0)
shapeX = int(shape_position_x[0])
shapeY = shape_position_y.pop(0)
shapeY = int(shape_position_y[0])
nextPos()

#Shape 13
begin()

t.begin_fill()
t.fillcolor(turtle_color[0])
t.goto(shapeX, shapeY)
t.back(133.3)
t.goto(start_x, start_y)
turtle_color.pop(0)
t.end_fill()

#Keeping whats on the screen there and hiding turtle
t.hideturtle()
wn = trtl.Screen()
wn.mainloop()