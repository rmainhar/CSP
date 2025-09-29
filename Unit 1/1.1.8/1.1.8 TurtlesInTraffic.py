#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
turtle = trtl.Turtle()
turtle.hideturtle()

print("Turtles are going to be in traffic.")

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["gold", "purple", "orange", "green", "blue", "red"]

tloc = -180
for s in turtle_shapes:
  #sets turtles color to new one from list and goes to new position
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-180, tloc)
  ht.setheading(0)
  

  #changes the color to new vertical one and to new position
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 180)
  vt.setheading(270)
  
  
  #position setter
  tloc += 60

# TODO: move turtles across and down screen, stopping for collisions
speed = 0

for i in range(300):
	#Move horizontal turtles forward
  for ht in horiz_turtles:
    turtle.speed(speed)
    ht.forward(15)
    speed = speed + 2
    if speed >= 10:
      speed = 0
    ht._update()
    if ((ht.xcor() - vt.ycor() < 20)):
      ht.color("pink")
      break
      '''horiz_turtles.remove(ht)'''
    
    if (ht.xcor() >= 200):
      ht.penup()
      ht.goto(180,ht.ycor())

  #move vertical turtles forward
  for vt in vert_turtles:
    turtle.speed(speed)
    vt.forward(10)
    speed = speed + 1
    if speed >= 10:
      speed = 0
    vt._update()
    if ((vt.xcor() + ht.ycor() < 20)):
      vt.color("black")
      break
      '''vert_turtles.remove(vt)'''
      
    if (vt.ycor() <= -200):
      vt.penup()
      vt.goto(vt.xcor(),-180)
  
print("Turtles are through traffic.")

wn = trtl.Screen()
wn.mainloop()