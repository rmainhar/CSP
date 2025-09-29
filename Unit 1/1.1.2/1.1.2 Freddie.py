#setting up turtle
import turtle as trtl
t = trtl.Turtle()

#making center circle
t.pensize(5)
t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

#make green stem
t.color("green")
t.fillcolor("green")
t.penup()
t.goto(15,-30)
t.pendown()
t.right(90)
t.begin_fill()
for i in range(2):
  t.forward(150)
  t.right(90)
  t.forward(30)
  t.right(90)
t.end_fill()

#making flower pedles
t.color("pink")
t.fillcolor("pink")
t.penup()
t.goto(0,50)
t.pendown()
t.begin_fill()
for i in range (6):
  t.left(60)
  for i in range(2):
    t.circle(80,90)
    t.circle(30,90)
t.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()