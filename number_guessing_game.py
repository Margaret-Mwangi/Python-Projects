#Generate a random number between 1 and 100
#Request the player to guess a number between 1 and 100
#If player number is greater than random number == Too High
#If player number is lower that random number == Too Low
#If player number == random number , then 'Congratulations!, you guessed the number'
#If the value from the player is not a number, then 'Enter a valid number'
#Game should only exit if the player gets it right

import random

generated_number = random.randint(1,100)

while True:
    try:
        player_guess = int(input("Guess a number between 1 and 100: "))

        if player_guess > generated_number:
            print("Too high!")
        elif player_guess < generated_number:
            print("Too Low!")
        else :
            print("Congratulations!, you guessed the number")
            break
            
    except ValueError:
        print("Enter a valid number")