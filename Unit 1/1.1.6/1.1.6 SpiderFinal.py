import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)

#spider body
painter.begin_fill()
painter.circle(50)
painter.end_fill()

#spider head
painter.penup()
painter.goto(0,-20)
painter.pendown()
painter.begin_fill()
painter.circle(20)
painter.end_fill()

#spider eyes
painter.penup()
painter.goto(-5,-20)
painter.pendown()
painter.fillcolor("red")
painter.begin_fill()
painter.circle(5)
painter.end_fill()
painter.penup()
painter.goto(5,-20)
painter.pendown()
painter.begin_fill()
painter.circle(5)
painter.end_fill()
painter.penup()
painter.goto(0,25)
painter.pendown()

#variables for legs
angle = 90

#spider legs left
for i in range(4):
  painter.setheading(angle)
  painter.circle(50,180)
  painter.penup()
  painter.goto(0,25)
  painter.pendown()
  angle = angle + 25
  
angle = 270
  

#spider legs right
for i in range(4):
  painter.setheading(angle)
  painter.circle(50,-180)
  painter.penup()
  painter.goto(0,25)
  painter.pendown()
  angle = angle - 25



'''# draw curved arc
painter.penup()
painter.goto(0, -20)
painter.pendown()
painter.circle(100, 180)

# draw segmented arc 
painter.penup()
painter.goto(0, 20)
painter.pendown()
painter.circle(100, 180, 3)'''

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()