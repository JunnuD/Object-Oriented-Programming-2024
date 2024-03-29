# LapTop computer
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

#Define new class that inherits the one above
class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self.__weight = weight
        
    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        # Customize the string representation
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"

# Example usage:
laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)
    