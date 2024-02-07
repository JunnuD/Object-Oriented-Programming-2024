class NumberStats:
    def __init__(self):
        # Change the initialization to an empty list
        self.numbers = []

    def add_number(self, number: int):
        # Append the number to the list [Tää täyty lisätä ite kun ei toiminut Itsin koodi]
        self.numbers.append(number)

    def count_numbers(self):
        # Return the length of the list
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)
    
    def separate_sum(self): # Part 4
        even_sum = sum(num for num in self.numbers if num % 2 == 0)
        odd_sum = sum(num for num in self.numbers if num % 2 != 0)
        return even_sum, odd_sum
        
        
if __name__ == "__main__":
    # Part 1 test prints:
    stats = NumberStats()
    """stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())"""

    #Part 2 test prints:
    stats = NumberStats()
    """stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())"""
    

while True:
    user_input = input("Enter an number to the list (-1 to close): ")
    if user_input == "-1":
           break
    try:
        number = int(user_input)
        stats.add_number(number)
    except ValueError:
            print("Invalid input. Please enter a valid integer. ")
        
print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())

even_sum, odd_sum = stats.separate_sum()
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)