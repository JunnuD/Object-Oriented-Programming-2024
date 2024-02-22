class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} g)"


# Part 1 testing...
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
print("Name of the book:", book.name())
print("Weight of the book:", book.weight())
print("Book:", book)
print("Phone:", phone)
print()
print("Part 1 päättyy")
print()


class Suitcase:
    def __init__(self, max_weigth: int):
        self.__max_weight = max_weigth
        self.__items = []
    
    def add_item(self, item: Item):
        if self.get_current_weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)
    
    def get_current_weight(self):
        return sum(item.weight() for item in self.__items)
    
    def __str__(self):
        num_items = len(self.__items)
        if num_items == 0:
            return f"0 items (o g)"
        elif num_items == 1:
            return f"1 item ({self.get_current_weight()} g)"
        else:
            return f"{num_items} items ({self.get_current_weight()} g)"
        
    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.get_current_weight()
    
    def heaviest_item(self):
        if not self.__items:
            return None
        else:
            return max(self.__items, key=lambda item: item.weight())




        
# Testing part 2 and 3...
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

suitcase = Suitcase(1000)
print(suitcase)
suitcase.add_item(book)
print(suitcase)
suitcase.add_item(phone)
print(suitcase)
suitcase.add_item(brick)
print(suitcase)
print()
print("Part 3 päättyy")
print()

# Testing part 4 and 5
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

suitcase = Suitcase(5000)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

print("The suitcase contains the following items:")
suitcase.print_items()

combined_weight = suitcase.weight()
print(f"Combined weight: {combined_weight} g")
heaviest = suitcase.heaviest_item()
print(f"The heaviest item: {heaviest}")

print()
print("Part 4 ja 5 päättyy")
print()




class CargoHold:
    def __init__(self, max_weigth: int):
        self.__max_weight = max_weigth
        self.__suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() <= self.__max_weight - self.get_current_weight():
            self.__suitcases.append(suitcase)

    def get_current_weight(self):
        return sum(suitcase.weight() for suitcase in self.__suitcases)
    
    def print_items(self):
        for suitcase in self.__suitcases:
            print(f"The items in the suitcase:")
            suitcase.print_items()
            print()

    def __str__(self):
        num_suitcases = len(self.__suitcases)
        available_space = self.__max_weight - self.get_current_weight()
        return f"{num_suitcases} suitcase{'s' if num_suitcases != 1 else ''}, space for {available_space} kg"

# Testing CargoHold... Part 6
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(5000)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()
print()
print("Part 6 päättyy ja vika osa alkaa")
print()


# Testing CargoHold... PT7
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(100)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()