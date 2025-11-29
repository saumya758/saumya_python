class Animal:
    def sound(self):     # polymorphic method
        return "Some sound"

class Dog(Animal):       # inheritance
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Encapsulation Example
class Person:
    def __init__(self, name, age):
        self.__age = age         # private variable
        self.name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

# Demonstration
a = [Dog(), Cat()]
for obj in a:
    print(obj.sound())   # polymorphism
