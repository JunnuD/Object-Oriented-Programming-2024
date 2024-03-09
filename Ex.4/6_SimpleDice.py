# Dice roll - program!
# 3 dices, calculate the sum and play for a winner

import random

class Dice:
    def __init__(self):
        self.value = 0  # Initial value before the first roll

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

def roll_all_dices(dices):
    return [dice.roll() for dice in dices]

def show_dice_values(dice_values):
    for i, value in enumerate(dice_values, start=1):
        print(f"Rolled number for dice {i}: {value}")

def tiebreaker(dices):
    print("Tiebreaker initiated...")
    while True:
        dice_values = roll_all_dices(dices)
        show_dice_values(dice_values)
        if len(set(dice_values)) == 1:  # If there's still a tie, roll again
            print("Tie in tiebreaker, rolling again...\n")
        else:
            winner_dice = dice_values.index(max(dice_values)) + 1
            print(f"Tiebreaker winner is dice {winner_dice} with value {max(dice_values)}\n")
            break

def play_game():
    num_dice = int(input("Enter the number of dice: "))
    dices = [Dice() for _ in range(num_dice)]

    total_round_sums = []
    for round_number in range(1, 4):  # 3 rounds
        print(f"\nRound {round_number}")
        dice_values = roll_all_dices(dices)
        round_sum = sum(dice_values)
        total_round_sums.append(round_sum)
        show_dice_values(dice_values)
        print(f"Round sum: {round_sum}")

    # Check for tie after all rounds are completed
    if len(set(total_round_sums)) == 1:  # Indicates a tie
        tiebreaker(dices)
    else:
        max_sum = max(total_round_sums)
        winner_round = total_round_sums.index(max_sum) + 1
        print(f"\nWinner is found in round {winner_round} with the highest sum: {max_sum}")

       
class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice()  # Each player has one dice
        self.pet = None  # Will be set in Part 5
    
    def roll_dice(self):
        return self.dice.roll()
    
    def set_pet(self, pet):
        self.pet = pet
    
    def __str__(self):
        return f"Player {self.player_id}: {self.name}, Pet: {self.pet}"
        
        
class Mammal:
    def __init__(self, ID, species, name, size, weight):
        self.ID = ID
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight
    
    def __str__(self):
        return f"Mammal: {self.species}, Name: {self.name}, Size: {self.size}, Weight: {self.weight}kg"
       
def create_mammals():
    # Create a list of mammals, sorted by weight so the selection can be based on dice roll
    return [
        Mammal(ID=1, species="Rabbit", name="Bun", size="Small", weight=2),
        Mammal(ID=2, species="Cat", name="Whiskers", size="Medium", weight=5),
        Mammal(ID=3, species="Dog", name="Barky", size="Medium", weight=10),
        Mammal(ID=4, species="Deer", name="Bambi", size="Large", weight=70),
    ]

def select_pet_for_player(player, mammals):
    # Roll two dices to determine the pet
    dice1, dice2 = Dice(), Dice()
    roll_sum = dice1.roll() + dice2.roll()
    print(f"{player.name} rolled a {roll_sum} selecting a pet.")

    # Select a pet based on the dice roll, mapping the roll sum to the list of mammals
    # Assuming a direct mapping for simplicity, but you could create a more complex selection mechanism
    selected_index = min(roll_sum-2, len(mammals)-1)  # -2 because minimum roll sum is 2, and we adjust for list index
    selected_pet = mammals[selected_index]
    player.set_pet(selected_pet)
    print(f"{player.name} now has a pet: {selected_pet}")

def main():
    # Create players
    players = [Player("Alice", 1), Player("Bob", 2)]

    # Create mammals
    mammals = create_mammals()

    # Assign a pet to each player
    for player in players:
        select_pet_for_player(player, mammals)

    # Print out each player and their pet's information
    for player in players:
        print(player)

if __name__ == "__main__":
    main()