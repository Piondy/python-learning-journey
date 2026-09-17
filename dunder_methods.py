# EASY — __str__
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"My dog is {self.name}"

dog = Dog("Buddy")
print(dog)

# MEDIUM — __len__
class Box:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return self.items
box = Box(10)
print(len(box))

# DIFFICULT — __eq__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

student1 = Student("Alex", 20)
student2 = Student("Alex", 20)
student3 = Student("John", 18)
print(student1 == student2)
print(student1 == student3)
