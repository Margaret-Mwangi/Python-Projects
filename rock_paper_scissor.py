#Randomly select a value between r, p and s
#Ask the user to make a choice between 3 options (r/p/s)
#If user enters anything else other than the 3 options, print ("Invalid Choice") and ask the user to choose again
#If random_option = s and user_choice = p, then , print('You win')
#If random_option = r and user_choice = s,  then, print("You win")
#If random option = p and user_choice = r, then, print ("You win!")
#Otherwise, print ("You lose")

import random

ROCK = "r"
PAPER = "P"
SCISSORS = "s"

emojis = {ROCK: "🗿" , SCISSORS: "✂" , PAPER : "📃"}
option_values = tuple(emojis.keys())

def get_player_choice():
    while True:
        player_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
        if player_choice in option_values:
            return player_choice
        else:
            print("Invalid Choice")

def display_choices(player_choice, computer_choice):
    print(f"You chose {emojis[player_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(player_choice, computer_choice):
    if ( 
        (computer_choice == PAPER and player_choice == SCISSORS) or 
        (computer_choice == SCISSORS and player_choice == ROCK) or 
        (computer_choice == ROCK and player_choice == PAPER) ):
        print("You win!")
        
    elif computer_choice == player_choice:
        print("It's a tie!! This is very interesting")
       
    else:
        print("You lose")

def play_game(): 
    while True:
        print(">>> play_game() function is now running <<<")
        player_choice = get_player_choice()
        
        computer_choice = random.choice(option_values)

        display_choices(player_choice, computer_choice)

        determine_winner(player_choice, computer_choice)
            
        play_more = input("Continue? (y/n): ")
        if play_more == "n":
            break

if __name__ == "__main__":
    print("script has started")
    play_game()
    print("Game has ended, thanks for playing! Bye")