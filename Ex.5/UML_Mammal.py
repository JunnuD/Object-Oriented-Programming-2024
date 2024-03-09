class Mammal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        print(f"{self.name} is moving.")

class Cat(Mammal):
    def purr(self):
        print(f"{self.name} is purring.")

class Dog(Mammal):
    def bark(self):
        print(f"{self.name} is barking.")

class Elephant(Mammal):
    def __init__(self, name, age, gender, trunkLength):
        super().__init__(name, age, gender)
        self.trunkLength = trunkLength

    def sprayWater(self):
        print(f"{self.name} is spraying water with its trunk.")
class Habitat:
    def __init__(self, environment):
        self.environment = environment

class Prey:
    def __init__(self, prey):
        self.prey = prey

# Examples 
cat = Cat("Whiskers", 3, "Female")
cat.eat()
cat.purr()

dog = Dog("Rex", 5, "Male")
dog.sleep()
dog.bark()

elephant = Elephant("Dumbo", 10, "Male", 1.5)
elephant.move()
elephant.sprayWater()
