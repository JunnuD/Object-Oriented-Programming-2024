import random

class Mouse:
    def __init__(self):
        self.caught = False

    def get_caught(self):
        # Let's say there's a 50% chance the mouse gets caught
        self.caught = random.choice([True, False])
        if self.caught:
            return "Mouse caught"
        else:
            return "Mouse escaped"


class Cat:
    def observe_prey(self, prey):
        # Observing the prey, which in this case is a mouse
        return f"Observing {type(prey).__name__}"

    def hunt(self, prey):
        if isinstance(prey, Mouse):
            action = prey.get_caught()
            if action == "Mouse caught":
                return "Successfully caught the prey"
            else:
                return "The prey escaped"

    def eat_prey(self, prey):
        if prey.caught:
            return "Eating prey"

    def clean(self):
        return "Cat cleaned up"

    def move_to_habitat(self, habitat):
        if isinstance(habitat, Habitat):
            habitat.receive_cat(self)
            return "Moved to habitat"

    def rest(self):
        return "Cat is resting"


class Habitat:
    def __init__(self):
        self.cats = []

    def receive_cat(self, cat):
        self.cats.append(cat)
        return "Cat back in habitat"


# Example how it would go
mouse = Mouse()
cat = Cat()
habitat = Habitat()

print(cat.observe_prey(mouse))
result = cat.hunt(mouse)
print(result)

if mouse.caught:
    print(cat.eat_prey(mouse))
else:
    print("Cat did not catch the mouse.")

print(cat.clean())
print(cat.move_to_habitat(habitat))
print(cat.rest())