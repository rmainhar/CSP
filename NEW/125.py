#125 Game - Squid Game Bridge
import turtle as trtl
import random as rand
from functools import partial

# --- Configuration & Setup ---

# Functions
def check_logic(clicked_turtle,bridge_index,x,y,):
    print(x,y,bridge_index)
    """Checks if the clicked bridge block is correct."""
    if bridge_index < len(bridge_logic):
        expected_logic = bridge_logic[bridge_index]
        if expected_logic:
            print(f"Correct! This block is safe.")
        else:
            print(f"Wrong! The block has shattered!")
            clicked_turtle.color("red")
            clicked_turtle.hideturtle()  # Hide the clicked turtle to simulate it shattering
    else:
        print("Invalid bridge index.")

# Lists
t_f = [True, False]
bridge_steps = []
bridge_logic = []

# Initialize Bridge Turtle
logic_index = 0
for i in range(10):
    #print(i)
    
    left_block = rand.choice(t_f)  
    right_block = not left_block  # Ensure the right block is the opposite of the left block  
    height = -200 + (i * 40)  # Adjust the height for each step
    for i in range(2):
        bridge = trtl.Turtle()
        bridge.penup()
        bridge.goto(-50 + i * 100, height)  # Position the blocks in a row
        bridge.shape("square")
        bridge.shapesize(stretch_wid=1, stretch_len=2)
        bridge.color("brown")
        bridge.showturtle()
        bridge_steps.append(bridge)
        bridge_logic.append(left_block if i == 0 else right_block)  # Store the logic for each block
        current_index = len (bridge_steps) - 1
        bridge.onclick(partial(check_logic,bridge, current_index))  # Bind the click event to the check_logic function
print(bridge_logic)

wn = trtl.Screen()
#wn.onclick(partial(check_logic,int(1)))
wn.listen()
wn.mainloop()