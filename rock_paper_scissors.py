import random

choices = ["rock", "paper", "scissors"]

def get_user_choice():
  while True:
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if user_choice in choices:
      return user_choice
    else:
      print("Invalid choice. Please enter rock, paper, or scissors.")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Tie"
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    return "You win!"
  else:
    return "You lose!"

# Main game loop
def play_game():
  print("Let's play Rock-Paper-Scissors!")

  user_choice = get_user_choice()
  computer_choice = random.choice(choices)

  print(f"You chose {user_choice}, computer chose {computer_choice}.")
  print(determine_winner(user_choice, computer_choice))

# Play the game
play_game()