class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

class Manga:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

class Anime:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

class Song:
    def __init__(self, name, artist, genre, year):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.year = year

# Example Usage:
python = Book("Fluent Python", "Luciana Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
IndepenceDay = Movie("Indepence Day", "Roland Emmerich","action", 1996 )

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")
print(f"{IndepenceDay.name}: {IndepenceDay.director} ({IndepenceDay.year})")

