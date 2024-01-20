# File: 1_coin.py
# Source: Tony Gaddis: Starting out with Python, 4th edition
# Modified by: Sanna Määttä & Anne Jumppanen
# Desc: Coin object tossing
# Author now: Junnu Danhammer

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"
        
    def toss_the_coin(self):
        if random.randint(0,4) == 0:
            self.sideup = "Heads"
        elif random.randint(0,4) == 1:
            self.sideup = "Upright!"
        elif random.randint(0,4) == 2:
            self.sideup = "Fell off the table and dissapeared"
        elif random.randint(0,3) == 3:
            self.sideup = "Defies gravity and flew to an wormhole in outer space"
        else:
            self.sideup = "Tails"
        
    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    
    print("This side is up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    
    print("Now this side is up:", my_coin.get_sideup())
    
main()