from collections import Counter

class ListHelper:
    
    @staticmethod
    def greatest_frequency(my_list):
        count_dict = Counter(my_list)
        most_common_item = max(count_dict, key=count_dict.get)
        return most_common_item        
    
    @staticmethod
    def doubles(my_list):
        count_dict = Counter(my_list)
        count_at_least_twice = sum(1 for count in count_dict.values() if count >= 2)
        return count_at_least_twice
        
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
