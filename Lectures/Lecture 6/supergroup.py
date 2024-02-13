class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superkyvyt: {self.superpowers}'

class SuperGroup:
    def __init__(self, name: str, home_place: str):
        self._name = name
        self._home_place = home_place
        self._members = []

    @property
    def name(self):
        return self._name

    @property
    def home_place(self):
        return self._home_place

    def add_member(self, hero: SuperHero):
        self._members.append(hero)


    def printing_group(self):
        print(f"{self.name}, {self.home_place}")
        print('Members: ')
        for member in self._members:
            print(member)

if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, Superstrenght")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)


    revengers.printing_group()