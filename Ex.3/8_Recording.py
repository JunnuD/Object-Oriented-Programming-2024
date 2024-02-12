class Recording:
    def __init__(self, length):
        self.__length = length

    def length(self):
        return self.__length
    
    def set_length(self, new_length):
        self.__length = new_length



the_wall = Recording(43)
print(the_wall.length())

the_wall.set_length(44)
print(the_wall.length())