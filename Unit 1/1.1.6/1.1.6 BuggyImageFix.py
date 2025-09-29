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

legs = 6
length = 70
direction = 380 / legs
space = 0

("direction=", direction)
spider.pensize(5)

while (space < legs):
  ("direction*space=", direction*space)
  spider.goto(0,0)
  spider.setheading(direction*space) #angle of legs
  spider.forward(length) #spider legs
  space = space + 1
  
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop() 