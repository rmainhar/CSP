import random as rand
import turtle as trtl
from functools import partial

# --- Setup Screen ---
wn = trtl.Screen()
wn.title("Squid Game - Glass Bridge")
wn.setup(width=450, height=650)
wn.cv._rootwindow.resizable(False, False)

# --- Game State ---
total_rows = 10
current_row = 0
score = 0
game_mode = 1  # Mode 1: Instant Death | Mode 2: Score / Retry
game_over = False
bridge_steps = []

# --- Scoreboard ---
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)

# --- Player ---
player = trtl.Turtle()
player.shape("circle")
player.penup()


def update_hud():
    """Updates top status display based on mode and state."""
    score_writer.clear()
    mode_name = "Instant Death" if game_mode == 1 else "Score Mode"

    if game_over and current_row < total_rows:
        score_writer.write(
            f"GAME OVER! [{mode_name}]\nPress 'R' to Restart",
            align="center",
            font=("Arial", 11, "bold"),
        )
    elif game_over and current_row == total_rows:
        score_writer.write(
            f"🎉 YOU WIN! [{mode_name}]\nFinal Score: {score} | Press 'R' to Restart",
            align="center",
            font=("Arial", 11, "bold"),
        )
    else:
        if game_mode == 1:
            score_writer.write(
                f"Mode: Instant Death | Row: {current_row}/{total_rows}\n[Press 'R' to Reset]",
                align="center",
                font=("Arial", 10, "normal"),
            )
        else:
            score_writer.write(
                f"Score: {score} | Row: {current_row}/{total_rows}\n[Press 'R' to Reset]",
                align="center",
                font=("Arial", 10, "normal"),
            )


def check_logic(clicked_turtle, row_num, is_safe, x, y):
    """Handles logic based on chosen game mode."""
    global current_row, score, game_over

    if game_over or row_num != current_row:
        return

    if is_safe:
        score += 100
        clicked_turtle.color("lime")
        player.goto(clicked_turtle.xcor(), clicked_turtle.ycor())
        current_row += 1

        # Win condition
        if current_row == total_rows:
            game_over = True
            player.goto(0, 220)

        update_hud()
    else:
        clicked_turtle.color("red")
        clicked_turtle.hideturtle()

        if game_mode == 1:
            # Mode 1: Instant Death
            game_over = True
            player.color("darkred")
            player.goto(clicked_turtle.xcor(), clicked_turtle.ycor())
            update_hud()
        else:
            # Mode 2: Deduct points, stay on current row so player can guess again
            score = max(0, score - 50)
            update_hud()


def build_bridge():
    #Generates new bridge tiles.
    global bridge_steps
    bridge_steps.clear()

    for row_idx in range(total_rows):
        left_safe = rand.choice([True, False])
        right_safe = not left_safe
        height = -200 + (row_idx * 40)

        for side in range(2):
            is_safe = left_safe if side == 0 else right_safe
            x_pos = -50 if side == 0 else 50

            bridge = trtl.Turtle()
            bridge.penup()
            bridge.goto(x_pos, height)
            bridge.shape("square")
            bridge.shapesize(stretch_wid=1, stretch_len=2)
            bridge.color("brown")

            bridge_steps.append(bridge)
            bridge.onclick(partial(check_logic, bridge, row_idx, is_safe))
        #print(left_safe,right_safe)


def reset_game():
    #Prompts player for mode choice and sets up new round.
    wn.tracer(0)  # Disable animation for pop-up input
    global current_row, score, game_over, game_mode

    # Prompt user for mode input
    choice = wn.textinput(
        "Select Game Mode",
        "Choose Mode:\n1 - Instant Death (1 mistake = Game Over)\n2 - Score Mode (Retry allowed on mistake)",
    )

    if choice == "2":
        game_mode = 2
    else:
        game_mode = 1  # Default to Mode 1

    # Re-enable keyboard listener after pop-up text input closes
    wn.listen()

    # Clear old tiles
    for tile in bridge_steps:
        tile.hideturtle()

    current_row = 0
    score = 0
    game_over = False

    player.color("cyan")
    player.goto(0, -240)

    build_bridge()
    update_hud()
    wn.tracer(1)  # Re-enable animation


# Initial start
reset_game()


# Bind key controls
wn.onkey(reset_game, "r")
wn.listen()
wn.mainloop()