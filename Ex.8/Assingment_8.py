class Mammal:
    def __init__(self):
        self.state = "Resting"

    def resting(self):
        print("The mammal is resting.")
        event = input("Is the mammal hungry? (yes/no): ").lower()
        if event == "yes":
            self.state = "Hungry"
        else:
            self.state = "Resting"

    def alert(self):
        print("The mammal is alert.")
        event = input("Is there no threat? (yes/no): ").lower()
        if event == "yes":
            self.state = "Resting"
        else:
            self.state = "Alert"

    def hungry(self):
        print("The mammal is hungry and starts searching for food.")
        event = input("Does the mammal find food? (yes/no): ").lower()
        if event == "yes":
            self.state = "Eating"
        else:
            self.state = "Searching for Food"

    def searching_for_food(self):
        print("The mammal is searching for food.")
        event = input("Does the mammal find food? (yes/no): ").lower()
        if event == "yes":
            self.state = "Eating"
        else:
            print("The mammal keeps searching for food.")
            self.state = "Searching for Food"

    def hunting(self):
        print("The mammal is hunting.")
        event = input("Does the mammal catch the prey? (yes/no): ").lower()
        if event == "yes":
            self.state = "Eating"
        else:
            print("The mammal does not catch the prey and goes back to resting.")
            self.state = "Resting"

    def eating(self):
        print("The mammal is eating.")
        event = input("Is the mammal satiated? (yes/no): ").lower()
        if event == "yes":
            print("The mammal is now satiated and goes to rest.")
            self.state = "Resting"
        else:
            print("The mammal is still hungry.")
            self.state = "Searching for Food"

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
