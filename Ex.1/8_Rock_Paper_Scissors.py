#Rock paper scissors
#Play until either you or the computer gets 3 wins. 
#Generate random number to get computer’s choice, then check who wins and keep track of victories.

# Author: Junnu Danhammer
# Description: Above!

import random
import sys

def get_users_choice():
    choice = input("Give your choice (R, P, S): ")
    while choice not in ["R", "P", "S"]:
        choice = input(f"Invalid choice. Please enter R, P or S: ")
    return choice

def get_computers_choice():
    return random.choice(["R", "P", "S"])
    
def get_round_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "R" and computer_choice == "S") or \
         (user_choice == "P" and computer_choice == "R") or \
         (user_choice == "S" and computer_choice == "P"):
             return "User"
    else:  
        return "Computer"
        
def get_scoreboard(winner, scores):
    if winner == "User":
        scores["User"] += 1
    elif winner == "Computer":
        scores["Computer"] += 1
    
def main():
    scores = {"User": 0, "Computer": 0}
    while scores["User"] < 3 and scores["Computer"] < 3:
        user_choice = get_users_choice()
        computer_choice = get_computers_choice()
        winner = get_round_winner(user_choice, computer_choice)
        
        get_scoreboard(winner, scores)
        
        if winner == "Tie":
            print(f"Computers choice is {computer_choice}. It's a tie! ")
            
        else:
            result_message = "Paper covers Rock." if computer_choice == 'P' else "Rock crushes Scissors." if computer_choice == 'R' else "Scissors cuts Paper."
            print(f"Computer's choice is {computer_choice}. {result_message} Computer {scores['Computer']} You {scores['User']}")
            
    if scores['User'] == 3:
            print("Congratulations! You won!")
            print()
    else:
        print("You lost!")
        print("Well done anyway.")
        
if __name__ == "__main__":
    main()
    sys.exit()