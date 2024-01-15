# Dice roll - program!
#Code a function that returns a random number between 1-6 when calling it. 
# Print out the number where the function is called (so do not print the number inside the function). 

# Author: Junnu Danhammer
# Description: Above!

import random

def roll_dice():
    return random.randint(1, 6)

dice_roll = roll_dice()
print("Rolled number: ", dice_roll)


