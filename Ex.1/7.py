# Process with an arithmetic progression (AP) 3, 6, 9, .... The maximum value of the AP is obtained from the user. 
# Count the number of terms that appeared in the AP, the sum of the terms and the sum of the squared terms. 
# Use functions in your solution.

# Author: Junnu Danhammer
# Description: Above!

def get_max_value():
    number = int(input("Give maximum value: "))
    return number

def calculate_progression(max_value):
    term = 3
    progression = []
    while term <= max_value:
        progression.append(term)
        term += 3
    return progression

def main_program():
    max_value = get_max_value()
    progression = calculate_progression(max_value)
    number_of_terms = len(progression)
    sum_of_terms = sum(progression)
    sum_of_squared_terms = sum(x**2 for x in progression)
    print(f"Procession is: {', '.join(map(str, progression))}")
    print(f"Number of terms: {number_of_terms}")
    print(f"Sum of terms: {sum_of_terms}")
    print(f"Sum of squared terms: {sum_of_squared_terms}")

main_program()