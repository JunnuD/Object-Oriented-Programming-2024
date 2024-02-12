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

        tietokone = random.randint(0,99)
        upright = 0
        heads = 0
        # Lisää tänne loput


        for i in range (10000):
            tietokone = random.randint(0,99)
            if tietokone < 40:
                self.sideup = "Heads"
                heads += 1
            elif tietokone < 80:
                self.sideup = "Tails!"
            elif tietokone < 90:
                self.sideup = "Fell off the table and dissapeared"
            elif tietokone < 98:
                self.sideup = "Upright"
                upright += 1
            else:
                self.sideup = "Defies gravity and flew to an wormhole in outer space"
        # Sisälle laskuri jokaiselle arvolle.
            
        print(upright)
        print(heads)

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    
    print("This side is up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    
    print("Now this side is up:", my_coin.get_sideup())
    
main()