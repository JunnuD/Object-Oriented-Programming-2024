class Pet:
    def __init__(self, name, species, year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth
        

def new_pet(name, species, year_of_birth):
    return Pet(name, species, year_of_birth)

fluffy = new_pet("Fluffy", "Dog", 2017)
print(fluffy.name)
print(fluffy.species) 
print(fluffy.year_of_birth)
    