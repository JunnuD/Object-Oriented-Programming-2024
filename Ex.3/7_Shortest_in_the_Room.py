class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    
class Room:
    def __init__(self):
        self.persons = []
  
    def add (self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        if self.is_empty():
            print("The room is empty")
        else:
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(person.height for person in self.persons)} cm.")
        for person in self.persons:
            print(f"{person.name}({person.height} cm)")
            
    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = min(self.persons, key=lambda x: x.height)
            return shortest_person
        
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = self.shortest()
            self.persons.remove(shortest_person)
            return shortest_person.name

# Usage example last Part
room = Room()
print("Is the room empty?", room.is_empty())

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest().name)
removed = room.remove_shortest()
print(f"Removed from room: {removed}")
print()
room.print_contents()