#a116_buggy_image.py
import turtle as trtl
#instead of a descriptive name of the turtle such as painter,
#a less useful variable name x is used
spider = trtl.Turtle()

#making body center in the center
spider.penup()
spider.goto(0,-20)
spider.pendown()

#making body
spider.pensize(40)
spider.circle(20)

#moving to head area
spider.penup()
spider.goto(0,30)
spider.pendown()

#making head
spider.pensize(20)
spider.circle(10)

#making the red eyes
spider.penup()
spider.goto(-5,40)
spider.pendown()
spider.fillcolor("red")
spider.begin_fill()
spider.pensize(5)
spider.circle(5)
spider.end_fill()
spider.penup()
spider.goto(5,40)
spider.pendown()
spider.begin_fill()
spider.circle(5)
spider.end_fill()

#variables
legs = 8
length = 70
direction = 360 / legs
space = 0
space2 = 0
angle = 35

("direction=", direction)
spider.pensize(5)

#drawing spider
while (space < legs):
  if (space < 4):
    ("direction*space=", direction*space)
    spider.goto(0,0)
    spider.setheading(angle*space-67.5) #angle of legs

    spider.forward(length) #spider legs

    space = space + 1

  if (space >= 4):
    ("direction*space=", direction*space)
    spider.goto(0,0)
    spider.setheading(angle*space2+135) #angle of legs

    spider.forward(length) #spider legs
    
    space2 = space2 + 1
    space = space + 1

#end stuff
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop() 