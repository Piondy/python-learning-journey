# EASY — Basic Inheritance
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def eat(self):
        super().eat()
dog = Dog()
dog.eat()

# MEDIUM — Adding a Child Method
class Animal2:
    def eat(self):
        print("Eating...")

class Dog2(Animal2):
    def bark(self):
        print("Woof! Woof!")
dog2 = Dog2()
dog2.eat()
dog2.bark()

# DIFFICULT — Method Overriding
class Animal3:
    def sound(self):
        print("Some animal sound")
class Dog3(Animal3):
    def sound(self):
        print("Woof!")
dog3 = Dog3()
dog3.sound()