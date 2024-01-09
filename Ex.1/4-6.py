#Write a program which repeatedly reads integers until the user enters 0. 
#Print out the number of negative integers. Use functions in your solution. 

def read_integer():
    number = int(input("Give an number (0 to stop): "))
    return number
        
def count_negative(numbers):
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count

def count_evenintegers(numbers):
    count2 = 0
    for number in numbers:
        if number % 2 == 0:
            count2 +=1
    return count2

def count_divisiblebythree(numbers):
    count3 = 0
    for number in numbers:
        if number % 3 == 0:
            count3 +=1
    return count3

def main_program():
    mylist = []
    while True:
        number = read_integer()
        if number == 0:
            break
        mylist.append(number)

    count = count_negative(mylist)
    print("Number of negative integers in your typing: ", count)

    count2 = count_evenintegers(mylist)
    print("Number of even intergers in your typing: ", count2)

    count3 = count_divisiblebythree(mylist)
    print("Number of divisible by three in your typing: ", count3)

main_program()
    

