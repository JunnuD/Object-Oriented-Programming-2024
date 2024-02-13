from phonebook import PhoneBook
from file_handler import FileHandler

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("Lectures/Lecture 6/phonebook/phonebook.txt")  

        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 - Exit")
        print("1 - Add Entry")
        print("2 - Search by name")
        print("3 - Search by number")

    def add_entry(self):
        name = input("Name: ")
        number = input("Number: ")
        self.__phonebook.add_number(name, number)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries)

    
    def search(self):
        name = input("Name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("Number unknown")
        for number in numbers:
            print(number)

    def search_by_number(self):
        number = input("Number: ")
        name = self.__phonebook.number_search(number)
        if name == None:
            print("Number unknown")
        else:
            print(name)


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("Command: ")
            if command == "0":
                self.exit()
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_by_number()
            else:
                self.help()

    
if __name__ == "__main__":
    application = PhoneBookApplication()
    application.execute()