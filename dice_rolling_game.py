#Request for user input (y,n): anything else is invalid
#generate 2 numbers
import random


while True:
    user_choice = input('Roll the dice? (y/n): ').lower()
    if user_choice == 'y':
        first_roll = random.randint(1,6)
        second_roll = random.randint(1,6)
        print(f'({first_roll}, {second_roll})')
    elif user_choice == 'n':
        print('Thanks for playing')
        break
    else:
        print('Invalid Choice')