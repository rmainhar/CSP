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
def start(): #Going to where the turtle starts making each individual shape
  t.penup()
  t.goto(start_x, start_y)
  t.pendown()

def begin(): #Setting the start_x and start_y to a number in a list above so I don't have to write it so often
  start_x = int(start_position_x[0])
  start_y = int(start_position_y[0])
  start()

def nextPosition(): #Setting the next position of start()
  global start_x
  global start_y
  start_position_x.pop(0)
  start_position_y.pop(0)
  start_x = int(start_position_x[0])
  start_y = int(start_position_y[0])

#trying to make a create all shapes command
shapeX1 = [200,100,-100,-100,0]
shapeX2 = [100,-100,-200,-166.6,0]
shapeX3 = [0,0,0,-200,0]
shapeY1 = [100,100,100,100,0]
shapeY2 = [100,100,100,166.6,0]
shapeY3 = [-200,-200,-200,100,0]

startPosX1 = int(shapeX1[0])
startPosY1 = int(shapeY1[0])
startPosX2 = int(shapeX2[0])
startPosY2 = int(shapeY2[0])
startPosX3 = int(shapeX3[0])
startPosY3 = int(shapeY3[0])

def drawShapes_2(): 
  global startPosX1
  global startPosX2
  global startPosX3
  global startPosY1
  global startPosY2
  global startPosY3

  t.fillcolor(turtle_color[0])
  t.begin_fill()

  t.goto(startPosX1,startPosY1)
  shapeX1.pop(0)
  shapeY1.pop(0)
  startPosX1 = int(shapeX1[0])
  startPosY1 = int(shapeY1[0])

  t.goto(startPosX2,startPosY2)
  shapeX2.pop(0)
  shapeY2.pop(0)
  startPosX2 = int(shapeX2[0])
  startPosY2 = int(shapeY2[0])

  t.goto(startPosX3,startPosY3)
  shapeX3.pop(0)
  shapeY3.pop(0)
  startPosX3 = int(shapeX3[0])
  startPosY3 = int(shapeY3[0])

  t.end_fill()
  turtle_color.pop(0)

#Use these computational skills
    #Use iteration (looping) and conditional execution (if statements) to control the drawing.
    #Have user interaction have an affect on your artwork
#Choose descriptive variable names.
#Comment code segments or blocks of statements.

#Setting everything up
for s in turtle_shape:
  t = trtl.Turtle(shape=s)#Called it t to save time
  t.color("light sky blue")
  t.pencolor("black")
t.pensize(5)

#Shapes 1 and 2
begin()
for i in range(13):
  drawShapes_2()

'''for i in range (2): 
  drawShapes_2()
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
nextPosition()

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
nextPosition()

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
nextPosition()

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
nextPosition()

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
nextPosition()

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
nextPosition()

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
nextPosition()

#Shape 13
begin()

t.begin_fill()
t.fillcolor(turtle_color[0])
t.goto(shapeX, shapeY)
t.back(133.3)
t.goto(start_x, start_y)
turtle_color.pop(0)
t.end_fill()'''

#Keeping whats on the screen there and hiding turtle
t.hideturtle()
wn = trtl.Screen()
wn.mainloop()