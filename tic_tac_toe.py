import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_win():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":  # Row check
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":  # Column check
            return True
    
    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    
    return False

# Function to check if the game is a draw
def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":  # If any button is empty
                return False
    return True

# Function to handle button clicks
def button_click(row, col):
    global game_over  # Declare game_over as global
    if buttons[row][col]['text'] == "" and not game_over:
        buttons[row][col]['text'] = current_player
        if check_win():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            game_over = True  # Set game_over to True when there is a winner
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            game_over = True  # Set game_over to True when it's a draw
        else:
            switch_player()

# Function to switch between players
def switch_player():
    global current_player  # Declare current_player as global
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Function to reset the game
def reset_game():
    global game_over, current_player  # Declare game_over and current_player as global
    game_over = False  # Reset game_over
    current_player = "X"  # Set current player back to X
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""  # Reset all buttons to empty

# Set up the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize game variables
game_over = False  # The game starts as not over
current_player = "X"  # Player "X" starts the game

# Create a 3x3 grid of buttons
buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Reset button to restart the game
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=20)

# Run the Tkinter event loop
root.mainloop()
