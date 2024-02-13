class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def number_search(self, number: str):
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name
        return None

    def all_entries(self):
        return self.__persons


phonebook = PhoneBook()
phonebook.add_number("Eric", "02-1233453")
print(phonebook.get_numbers("Eric"))
print(phonebook.get_numbers("Emily"))