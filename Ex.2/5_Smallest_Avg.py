def smallest_average(person1, person2, person3):
    def calculate_average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    averages = {
        "person1": calculate_average(person1),
        "person2": calculate_average(person2),
        "person3": calculate_average(person3)
    }

    min_avg_person = min(averages, key=averages.get)
    
    return locals()[min_avg_person]

# Example Usage:
person1 = {"name": "Alice", "result1": 2, "result2": 7, "result3": 9}
person2 = {"name": "Bob", "result1": 6, "result2": 8, "result3": 7}
person3 = {"name": "Charlie", "result1": 9, "result2": 6, "result3": 8}

winner = smallest_average(person1, person2, person3)
print("Winner:", winner)
