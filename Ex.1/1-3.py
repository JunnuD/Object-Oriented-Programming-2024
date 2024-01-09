#Is everything working?

# Start by installing your preferred IDE. Then write a code that prints out Hello
# in order to verify that your development environment is properly set up.
# If you already have IDE that you like, you can skip this exercise.

# 2.Code a list of at least 10 items 
# and fill it with numbers asked from user. Do the same with strings. Print out both lists. 
# Then fill the number list with randomly generated numbers and print it out. 

# 3. Arrange numbers in the list from smallest to largest and strings in alphabetical order and print out the lists.


import random

print()
print("Eeeellouu Mate!")
print()

numerolist = []
stringlist = []

for i in range(10):
    number = int(input("Please give a number: "))
    numerolist.append(number)

print(numerolist)

for i in range(10):
    string = input("Please give a string: ")
    stringlist.append(string)

print(stringlist)


numerolist.clear()

for i in range (10):
    random_numero = random.randint(1,100)
    numerolist.append(random_numero)

print()
print("Now the same list cleared and with random numbers: ", numerolist)

print("And now the number list sorted from smalles to biggest and the string list sorted in alphabetical order.")
numerolist.sort()
print(numerolist)

stringlist.sort()
print(stringlist)

