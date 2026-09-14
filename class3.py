class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)