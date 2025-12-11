import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"

# Change the dictionary keys to use the single-letter constants
emojis = {ROCK: "🪨", PAPER: "📃", SCISSORS: "✂️"} 
choices = tuple(emojis.keys()) # choices is now ("r", "p", "s")

def get_user_choice():
    while True:
        # The prompt is correct for r, p, s
        user_choice = input("Rock, Paper, or Scissors? (r,p,s): ").lower()
        if user_choice in choices: # This condition now works correctly
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    # This works now because the input matches the dictionary keys
    print(f"you chose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("tie!")
    elif (
      # The logic now compares using the correct single-letter constants (r, p, s)
      (user_choice == ROCK and computer_choice == SCISSORS) or
      (user_choice == SCISSORS and computer_choice == PAPER) or
      (user_choice == PAPER and computer_choice == ROCK)):
        print("You win")
    else:
       print("You lose")    

    
def play_game():
   while True:
     user_choice = get_user_choice()
     computer_choice = random.choice(choices)
     display_choices(user_choice, computer_choice)
     determine_winner(user_choice, computer_choice)
     should_continue = input("Continue? (y/n): ").lower()
     if should_continue == "n":
         break       
         
play_game()
