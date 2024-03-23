class Mammal:
    def __init__(self):
        self.state = "Resting"

    def resting(self):
        print("The mammal is resting.")
        # Event triggers
        event = input("What happens next? (Danger/Hungry): ").lower()
        if event == "danger":
            self.state = "Alert"
        elif event == "hungry":
            self.state = "Searching for Food"

    def alert(self):
        print("The mammal is alert.")
        event = input("What happens next? (No Threat/Decide to Hunt): ").lower()
        if event == "no threat":
            self.state = "Resting"
        elif event == "decide to hunt":
            self.state = "Hunting"

    def searching_for_food(self):
        print("The mammal is searching for food.")
        event = input("What happens next? (Finds Food/Cannot Find Food/Finds Prey): ").lower()
        if event == "finds food":
            self.state = "Eating"
        elif event == "cannot find food":
            self.state = "Searching for Food"
        elif event == "finds prey":
            self.state = "Hunting"


    def hunting(self):
        print("The mammal is hunting.")
        event = input("What happens next? (Catches Prey/Loses Prey/Tired): ").lower()
        if event == "catches prey":
            self.state = "Eating"
        elif event == "loses prey" or event == "tired":
            self.state = "Resting"

    def eating(self):
        print("The mammal is eating.")
        event = input("What happens next? (Satiated/Disturbed): ").lower()
        if event == "satiated":
            self.state = "Resting"
        elif event == "disturbed":
            self.state = "Alert"

    def run(self):
        # Main loop to simulate mammal's behavior
        while True:
            if self.state == "Resting":
                self.resting()
            elif self.state == "Alert":
                self.alert()
            elif self.state == "Searching for Food":
                self.searching_for_food()
            elif self.state == "Hunting":
                self.hunting()
            elif self.state == "Eating":
                self.eating()
            else:
                print("Undefined state. Exiting simulation.")
                break
            
            continue_simulation = input("Continue simulation? (yes/no): ").lower()
            if continue_simulation != "yes":
                print("Exiting simulation.")
                break

mammal = Mammal()
mammal.run()
