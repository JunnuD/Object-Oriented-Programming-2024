class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed
 
    def __str__(self):
        return f"Car (brand: {self.make}, top speed: {self.top_speed})"
    
    def fastest_car(self):
        if not cars:
            return None  # Return None if the list is empty
        return max(cars, key=lambda car: car.top_speed)
 
# Do your solution here:
    


if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

 
    cars = [car1, car2, car3, car4]
    fastest = Car.fastest_car(cars)
    if fastest:
        print(f"The fastest car is: {fastest}")
    else:
        print("No cars in the list.")