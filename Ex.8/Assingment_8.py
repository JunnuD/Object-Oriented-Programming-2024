import random

class Mammal:
    def __init__(self):
        self.state = "Resting"

    def resting(self):
        print("The mammal is resting.")
        # Randomly decide if the mammal becomes hungry or detects danger
        if random.choice(["Hungry", "Danger"]) == "Hungry":
            self.state = "Hungry"
        else:
            self.state = "Alert"

    def alert(self):
        print("The mammal is alert.")
        # Randomly decide if the threat passes or the mammal decides to hunt
        if random.choice(["No Threat", "Decide to Hunt"]) == "No Threat":
            self.state = "Resting"
        else:
            self.state = "Searching for Food"

    def hungry(self):
        print("The mammal is hungry and starts searching for food.")
        self.state = "Searching for Food"

    def searching_for_food(self):
        print("The mammal is searching for food.")
        # Randomly decide if the mammal finds food
        if random.choice(["Finds Food", "Cannot Find Food"]) == "Finds Food":
            self.state = "Eating"
        else:
            print("The mammal could not find food and decides to continue searching.")
            self.state = "Searching for Food"

    def hunting(self):
        print("The mammal is hunting.")
        # Randomly decide if the mammal catches prey
        if random.choice(["Catches Prey", "Loses Prey"]) == "Catches Prey":
            self.state = "Eating"
        else:
            print("The mammal loses the prey or gets tired and goes back to resting.")
            self.state = "Resting"

    def eating(self):
        print("The mammal is eating.")
        # Randomly decide if the mammal is satiated or disturbed
        if random.choice(["Satiated", "Disturbed"]) == "Satiated":
            print("The mammal is now satiated and goes to rest.")
            self.state = "Resting"
        else:
            print("The mammal is disturbed while eating and becomes alert.")
            self.state = "Alert"

    def run(self):
        # Main loop to simulate mammal's behavior
        while True:
            if self.state == "Resting":
                self.resting()
            elif self.state == "Alert":
                self.alert()
            elif self.state == "Hungry":
                self.hungry()
            elif self.state == "Searching for Food":
                self.searching_for_food()
            elif self.state == "Hunting":
                self.hunting()
            elif self.state == "Eating":
                self.eating()
            else:
                print("Undefined state. Exiting simulation.")
                break
            
            # Ask user to continue simulation or not
            continue_simulation = input("Continue simulation? (yes/no): ").lower()
            if continue_simulation != "yes":
                print("Exiting simulation.")
                break

# Create an instance of Mammal and run the simulation
mammal = Mammal()
mammal.run()
