import tkinter as tk
import random
from tkinter import messagebox

# --- Themes for Light and Dark modes ---
dark_theme = {
    "bg": "#1e1e1e",        # Background color
    "fg": "#ffffff",        # Foreground (text) color
    "btn_bg": "#333333",    # Button background
    "btn_fg": "#ffffff",    # Button text
    "entry_bg": "#2a2a2a"   # Input field background
}

light_theme = {
    "bg": "#ffffff",
    "fg": "#000000",
    "btn_bg": "#dddddd",
    "btn_fg": "#000000",
    "entry_bg": "#f0f0f0"
}

# Hint and success colors
HINT_COLOR = "#ff4b4b"
SUCCESS_COLOR = "#4bff4b"

# Start with dark theme
current_theme = "dark"
theme = dark_theme

# --- Game Variables ---
secret_number = random.randint(1, 100)  # Random number to guess
guess_count = 0                         # How many guesses used
guess_max = 10                          # Max allowed guesses

# --- Theme Toggle Function ---
def toggle_theme():
    global current_theme, theme

    # Switch theme based on current state
    theme = light_theme if current_theme == "dark" else dark_theme
    current_theme = "light" if current_theme == "dark" else "dark"

    # Update colors of widgets with new theme
    root.configure(bg=theme["bg"])
    starting_label.config(bg=theme["bg"], fg=theme["fg"])
    result_label.config(bg=theme["bg"], fg=theme["fg"])
    left_guesses.config(bg=theme["bg"], fg=theme["fg"])
    user_input.config(bg=theme["entry_bg"], fg=theme["fg"], insertbackground=theme["fg"])
    guess_button.config(bg=theme["btn_bg"], fg=theme["btn_fg"])
    restart_button.config(bg=theme["btn_bg"], fg=theme["btn_fg"])
    exit_button.config(bg=theme["btn_bg"], fg=theme["btn_fg"])
    theme_button.config(bg=theme["btn_bg"], fg=theme["btn_fg"])

    # Change button text to reflect new state
    theme_button.config(text="Dark Mode" if current_theme == "light" else "Light Mode")

# --- Reset the game state ---
def reset_game():
    global secret_number, guess_count
    secret_number = random.randint(1, 100)
    guess_count = 0

    # Enable input and clear previous guesses
    user_input.config(state='normal')
    guess_button.config(state='normal')
    user_input.delete(0, tk.END)
    result_label.config(text="", fg=theme["fg"])
    left_guesses.config(text=f"You have {guess_max} Guesses left !!", fg=theme["fg"], bg=theme["bg"])

# --- Main Game Logic ---
def guess_the_num():
    global guess_count

    # Validate input
    try:
        num = int(user_input.get())
    except ValueError:
        messagebox.showwarning("Warning", "Enter a number Only !!")
        return

    # If already out of guesses
    if guess_count >= guess_max:
        result_label.config(text=f"Game Over!! The number was {secret_number}", fg=HINT_COLOR)
        return

    # Correct guess
    if num == secret_number:
        result_label.config(text="🎉 Correct! You guessed the number!", fg=SUCCESS_COLOR)
        end_game()

    # Too high
    elif num > secret_number:
        result_label.config(text="Hint! : Lower Number Please !!", fg=HINT_COLOR)
        guess_count += 1

    # Too low
    else:
        result_label.config(text="Hint! : Higher Number Please !!", fg=HINT_COLOR)
        guess_count += 1

    # If all guesses are used and not correct
    if guess_count >= guess_max and num != secret_number:
        result_label.config(text=f"❌ Out of guesses! The number was {secret_number}", fg="red")
        end_game()

    # Update remaining guesses
    left_guesses.config(text=f"You have {guess_max - guess_count} left !!")
    user_input.delete(0, tk.END)

# --- Disable inputs once game ends ---
def end_game():
    user_input.config(state='disabled')
    guess_button.config(state='disabled')

# --- GUI SETUP ---
root = tk.Tk()
root.title("--- Guess The Number ---")
root.geometry('640x480')
root.resizable(False, False)
root.configure(bg=theme["bg"])

# Entry label
starting_label = tk.Label(root, text="Enter your guess here (1-100) :", bg=theme["bg"], fg=theme["fg"], font=("Arial", 12))
starting_label.pack(pady=5)

# Input box
user_input = tk.Entry(root, bg=theme["entry_bg"], fg=theme["fg"], insertbackground=theme["fg"], font=("Arial", 12))
user_input.pack(pady=5)

# Result feedback label
result_label = tk.Label(root, text="", bg=theme["bg"], fg=theme["fg"], font=("Arial", 12))
result_label.pack()

# Guesses left display
left_guesses = tk.Label(root, text=f"You have {guess_max} Guesses left !!", font=("Arial", 11), bg=theme["bg"], fg=theme["fg"])
left_guesses.pack()

# Guess submit button
guess_button = tk.Button(root, text="Submit Guess", command=guess_the_num, width=12, height=2, bg=theme["btn_bg"], fg=theme["btn_fg"])
guess_button.pack(pady=5)

# Restart button
restart_button = tk.Button(root, text="Restart Game", command=reset_game, width=12, height=2, bg=theme["btn_bg"], fg=theme["btn_fg"])
restart_button.pack(pady=5)

# Theme toggle button
theme_button = tk.Button(root, text="Light Mode", command=toggle_theme, width=12, height=2, bg=theme["btn_bg"], fg=theme["btn_fg"])
theme_button.pack(pady=5)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, width=12, height=2, bg=theme["btn_bg"], fg=theme["btn_fg"])
exit_button.pack(pady=5)

# Pressing Enter key submits the guess
root.bind('<Return>', lambda event: guess_the_num())

# Run the application
if __name__ == '__main__':
    root.mainloop()
