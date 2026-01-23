# Solution to week 02 questions
# CTRL + ` --> opens the terminal in VS Code
import random


choices = ["Rock", "Paper", "Scissors"]

player_choice = input("Enter your choice(press 1 for Rock, 2 for Paper, 3 for Scissors).\n")
player_choice = int(player_choice)
if player_choice < 1 or player_choice > 3:
    print("Invalid choice. Please select a number between 1 and 3.")
else:
    # Determine the winner logic using if-elif-else statements
    for counter in range(1, 4):
        print(f"You chose: {choices[player_choice - 1]}")
        computer_choice = random.randint(1, 3)
        print(f"Computer chose: {choices[computer_choice - 1]}")
        winner_choices = player_choice == 1 and computer_choice == 3 or player_choice == 2 and computer_choice == 1 or player_choice == 3 and computer_choice == 2
        if player_choice == computer_choice:
            print("It's a tie!")
        elif winner_choices:
            print("You win!")
        else:
            print("Computer wins!")
         