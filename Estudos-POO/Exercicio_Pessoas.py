class People:
    def __init__(self, name, age, height):
        self.name = name
        self.age = int(age)
        self.height = float(height)
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

class Rectangle:
    def __init__(self, height, width):
        self.width = int(width)
        self.height = int(height)

    def area(self):
        return f"Area: {self.width * self.height}"
    
    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"
    
person = People("Pedro", "17", "1.75")
print(person)

rectangle = Rectangle(10, 10)
print(f"{rectangle}, {rectangle.area()}")