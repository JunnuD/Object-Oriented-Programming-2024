def by_credits_and_id(student):
    return(-student["Credits"], student["id"][::-1])

if __name__== "__main__":
    students_data = [
    {"Name": "Marvin","id": "M321", "Credits": 220},
    {"Name": "Anna", "id": "A999", "Credits": 220},
    {"Name":"Eric", "id": "O453", "Credits": 120},
    {"Name":"Ben", "id": "L982", "Credits": 235},
    {"Name":"Archie", "id": "A123", "Credits": 220}
    ]

for student in sorted(students_data, key=by_credits_and_id):
    print(f"{student['Name']} ({student['id']}, {student['Credits']})cr.")