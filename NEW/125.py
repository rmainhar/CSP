import random as rand
import turtle as trtl
from functools import partial

# --- Configuration & Setup ---
wn = trtl.Screen()
wn.title("Squid Game - Glass Bridge")
wn.setup(width=400, height=600)
wn.cv._rootwindow.resizable(False, False)

# Game State Variables
current_step = 0
total_steps = 10

bridge_steps = []
bridge_logic = []

# --- Player Setup ---
player = trtl.Turtle()
player.shape("circle")
player.color("cyan")
player.penup()
player.goto(0, -240)


# --- Game Logic ---
def check_logic(clicked_turtle, step_num, is_safe, x, y):
    """Checks if the clicked bridge block is correct and in sequence."""
    global current_step

    # Enforce sequential stepping
    if step_num != current_step:
        print(f"You must complete step {current_step + 1} first!")
        return

    if is_safe:
        print(f"Step {step_num + 1}: Correct! Safe glass.")
        clicked_turtle.color("lime")
        player.goto(clicked_turtle.xcor(), clicked_turtle.ycor())
        current_step += 1

        # Win condition
        if current_step == total_steps:
            print("Congratulations! You safely crossed the bridge!")
            player.goto(0, 220)
    else:
        print(f"Step {step_num + 1}: Wrong! The glass shattered!")
        clicked_turtle.color("red")
        clicked_turtle.hideturtle()  # Hide shattered tile
        player.color("darkred")
        player.goto(clicked_turtle.xcor(), clicked_turtle.ycor())


# --- Build Bridge ---
for step_idx in range(total_steps):
    left_safe = rand.choice([True, False])
    right_safe = not left_safe

    height = -200 + (step_idx * 40)

    for side in range(2):  # 0 = Left, 1 = Right
        is_safe = left_safe if side == 0 else right_safe
        x_pos = -50 if side == 0 else 50

        bridge = trtl.Turtle()
        bridge.penup()
        bridge.goto(x_pos, height)
        bridge.shape("square")
        bridge.shapesize(stretch_wid=1, stretch_len=2)
        bridge.color("brown")

        bridge_steps.append(bridge)
        bridge_logic.append(is_safe)

        # Bind click with turtle object, step number, and safety status
        bridge.onclick(partial(check_logic, bridge, step_idx, is_safe))

wn.listen()
wn.mainloop()