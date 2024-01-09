#Is everything working?
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

