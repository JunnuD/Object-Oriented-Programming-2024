# Write a phone book application. It should work as follows:
# command (1 search, 2 add, 3 quit): 2 name: peter number: 040-5466745 ok!
# command (1 search, 2 add, 3 quit): 2 name: emily number: 045-1212344 ok!
# command (1 search, 2 add, 3 quit): 1 name: peter 040-5466745 
# command (1 search, 2 add, 3 quit): 1 name: maryno number
# command (1 search, 2 add, 3 quit): 2 name: peternumber: 09-22223333ok!
# command (1 search, 2 add, 3 quit): 1 name: peter09-22223333
# command (1 search, 2 add, 3 quit): 3 quitting...

#File name: 10_Phone_Book.py
# Author: Junnu Danhammer
# Description: Above!

def get_user_add(phone_book):
    while True:
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        
        if name and number:
            phone_book[name] = number
            print("Ok! ")
            break
        else:
            print("Invalid input. Both name and number are required.")
        
def get_user_search(phone_book):
    while True:
        name_to_search = input("Enter the name to search: ")

        if name_to_search in phone_book:
            print(f"Name: {name_to_search}, Number: {phone_book[name_to_search]}")
            break
        else:
            print(f"No entry found for {name_to_search} in the phone book.")
            break

def get_quit_program():
    print("Quitting...")
    
    
def main():
    phone_book = {}  # Initialize an empty phone book

    # Sample entries for testing
    phone_book["Peter"] = "040-5466745"
    phone_book["Emily"] = "045-1212344"

    while True:
        choice = input("Choose one --> 1: Search, 2: Add, 3: Quit ")

        if choice == "1":
            get_user_search(phone_book)
        elif choice == "2":
            get_user_add(phone_book)
        elif choice == "3":
            get_quit_program()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()