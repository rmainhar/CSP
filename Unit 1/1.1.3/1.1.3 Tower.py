#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

t = trtl.Turtle()
t.speed(0)
t.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 21

# iterate
for i in range(3): #to make other 2 towers
  for floor in range(num_floors):
    # set placement and color of turtle
    t.penup()
    t.goto(x, y)
    rem = floor % 9 #
    t.color("gray")
    if (rem == 3):
      t.color("blue")
    if (rem == 4):
      t.color("blue")
    if (rem == 5):
      t.color("blue")
    if (rem == 6):
      t.color("pink")
    if (rem == 7):
      t.color("pink")
    if (rem == 8):
      t.color("pink")
    y = y + 5 # location of next floor
    
    #draw the floor
    t.pendown()
    t.forward(50)
    
  #move to next tower
  x = x + 50
  y = -150

wn = trtl.Screen()
wn.mainloop()