class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def Animal_sound(self):
        return "generic sound"
    
    def __str__(self):
        return f"The name is: {self.name} and the color is: {self.color}"
    
class Dog(Animal):
    def Animal_sound(self):
        return "Auau"
    
class Cat(Animal):
    def Animal_sound(self):
        return "Miau"
    
cat = Cat("Lua", "Black")
dog = Dog("Zeus", "Black")
print(f"{cat}, {cat.Animal_sound()}\n{dog}, {dog.Animal_sound()}")