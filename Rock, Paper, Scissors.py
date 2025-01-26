import tkinter as tk
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def player_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    
    player_label.config(text=f"Your Choice: {choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)

def reset_game():
    player_label.config(text="Your Choice: ")
    computer_label.config(text="Computer's Choice: ")
    result_label.config(text="")

root = tk.Tk()
root.title("Rock Paper Scissors Game")

player_label = tk.Label(root, text="Your Choice: ", font=("Helvetica", 16))
player_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer's Choice: ", font=("Helvetica", 16))
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", command=lambda: player_choice("Rock"), font=("Helvetica", 14))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(root, text="Paper", command=lambda: player_choice("Paper"), font=("Helvetica", 14))
paper_button.pack(side=tk.LEFT, padx=20)

scissors_button = tk.Button(root, text="Scissors", command=lambda: player_choice("Scissors"), font=("Helvetica", 14))
scissors_button.pack(side=tk.LEFT, padx=20)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Helvetica", 14))
reset_button.pack(pady=20)

root.mainloop()