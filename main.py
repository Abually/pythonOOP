# Assignment 1: Design Your Own Class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB).")

    
    def read(self):
        print(f"Reading '{self.title}' on your device.")



class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


if __name__ == "__main__":
    
    book = Book("1984", "George Orwell", 328)
    ebook = EBook("Digital Fortress", "Dan Brown", 356, 2)
    book.read()
    book.info()
    ebook.read()
    ebook.download()

    print("\nPolymorphism Challenge:")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()