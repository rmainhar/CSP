#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()

#variables
legs = 6
length = 70
direction = 360 / legs
ladybug.pensize(5)
space = 0
space2 = 0
angle = 45

#drawing spider
while (space < legs):
  if (space < 3):
    ladybug.goto(0,-20)
    ladybug.setheading(angle*space-45) #angle of legs

    ladybug.forward(length) #spider legs

    space = space + 1

  if (space >= 3):
    ladybug.goto(0,-20)
    ladybug.setheading(angle*space2+135) #angle of legs

    ladybug.forward(length) #spider legs

    space2 = space2 + 1
    space = space + 1

# create ladybug head
ladybug.penup()
ladybug.goto(0,0)
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.setheading(0)
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25 #Had x and y

  xpos = xpos + 5 #Had x and y
  
  num_dots = num_dots + 1 #said num_dot not num_dots

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()