import tkinter as tk
from tkinter import messagebox

# ---------- Helper Functions ----------

def check_winner():
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in combos:
        if (buttons[combo[0]]["text"] ==
            buttons[combo[1]]["text"] ==
            buttons[combo[2]]["text"] != ""):
            return True
    return False


def button_click(i):
    global turn

    if buttons[i]["text"] == "" and not game_over:
        buttons[i].config(text="X" if turn else "O")
        if check_winner():
            end_game(f"Player {'X' if turn else 'O'} wins!")
        elif all(button["text"] != "" for button in buttons):
            end_game("It's a draw!")
        else:
            turn = not turn


def end_game(result):
    global game_over
    game_over = True
    messagebox.showinfo("Game Over", result)
    ask_restart()


def ask_restart():
    answer = messagebox.askyesno("Restart", "Do you want to play again?")
    if answer:
        reset_game()
    else:
        root.quit()


def reset_game():
    global turn, game_over
    turn = True
    game_over = False
    for button in buttons:
        button.config(text="")


def create_buttons(root):
    for i in range(9):
        button = tk.Button(
            root, text="", font=("Helvetica", 24),
            width=5, height=2, command=lambda i=i: button_click(i)
        )
        button.grid(row=i//3, column=i%3)
        buttons.append(button)


# ---------- Main Function ----------

def main():
    global root, buttons, turn, game_over
    root = tk.Tk()
    root.title("Tic Tac Toe")

    buttons = []
    turn = True
    game_over = False

    create_buttons(root)
    root.mainloop()


# ---------- Run Program ----------
if __name__ == "__main__":
    main()