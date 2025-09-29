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

#mking head
spider.pensize(20)
spider.circle(10)

#variables
legs = 8
length = 70
direction = 360 / legs
space = 0
right_angle = 35
left_angle = 180 #this isnt working yet

("direction=", direction)
spider.pensize(5)

#drawing spider
while (space < legs):
  if (space < 4):
    ("direction*space=", direction*space)
    spider.goto(0,0)
    spider.setheading(right_angle*space-67.5) #angle of legs

    spider.forward(length) #spider legs

    space = space + 1
  if (space >= 4): #this isnt working yet

    ("direction*space=", direction*space)
    spider.goto(0,0)
    spider.setheading(left_angle*space+67.5) #angle of legs

    spider.forward(length) #spider legs
    
    space = space + 1

#end stuff
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()