class Student:
    def __init__(self, name: str, id:str, credits: int):
        self.name = name
        self.id = id
        self.credits = credits
    

    def __str__(self):
        return f"{self.name} ({self.id} {self.credits})cr."

def by_id(item: Student):
    return item.id

def by_credits(item: Student):
    return item.credits

def by_credits_and_id(item: Student):
    return (item.credits, item.id)

if __name__== "__main__":
    o1 = Student("Archie", "A123", 220)
    o2 = Student("Marvin", "M321", 220)
    o3 = Student("Anna", "A999", 220)
    o4 = Student("Eric", "O453", 120)
    o5 = Student("Ben", "L982", 235)

    students = [o1, o2, o3, o4, o5]

    print("Sort by id: ")
    for student in sorted(students, key=by_id):
        print(student)

    print()
    print("Sort by credits: ")
    for student in sorted(students, key=by_credits):
        print(student)


    print()
    print("Sort by credits and ID: ")
    for student in sorted(students, key=by_credits_and_id):
        print(student)