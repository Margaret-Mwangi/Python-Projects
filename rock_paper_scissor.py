#Randomly select a value between r, p and s
#Ask the user to make a choice between 3 options (r/p/s)
#If user enters anything else other than the 3 options, print ("Invalid Choice") and ask the user to choose again
#If random_option = s and user_choice = p, then , print('You win')
#If random_option = r and user_choice = s,  then, print("You win")
#If random option = p and user_choice = r, then, print ("You win!")
#Otherwise, print ("You lose")

import random

option_values = ("r", "p", "s")
emojis = {"r": "🗿" , "s": "✂" , "p" : "📃"}

while True:
    
    player_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    play_more = ""
    if player_choice not in option_values:
        print("Invalid Choice")
        continue
    
    computer_choice = random.choice(option_values)

    print(f"You chose {emojis[player_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if ( 
        (computer_choice == "p" and player_choice == "s") or 
        (computer_choice == "s" and player_choice == "r") or 
        (computer_choice == "r" and player_choice == "p") ):
        print("You win!")
        
    elif computer_choice == player_choice:
        print("It's a tie!! This is very interesting")
       
    else:
        print("You lose")
        
    
    play_more = input("Continue? (y/n): ")
    if play_more == "n":
        break
        
