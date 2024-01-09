import random

def get_integer_input(prompt):
    """Get and return a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

print("\nEeeellouu Mate!\n")

# List for storing numbers
numerolist = []

# Getting numbers from the user
for i in range(10):
    number = get_integer_input(f"Please give number {i + 1}/10: ")
    numerolist.append(number)

print(numerolist)

# List for storing strings
stringlist = []

# Getting strings from the user
for i in range(10):
    string = input(f"Please give string {i + 1}/10: ")
    stringlist.append(string)

print(stringlist)

# Clearing the number list and adding random numbers
numerolist.clear()

for i in range(10):
    random_numero = random.randint(1, 100)
    numerolist.append(random_numero)

print("\nNow the same number list cleared and with random numbers:", numerolist)


print("And now the number list sorted from smalles to biggest and the string list sorted in alphabetical order.")
numerolist.sort()
print(numerolist)

stringlist.sort()
print(stringlist)

