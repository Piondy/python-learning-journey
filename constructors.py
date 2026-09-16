# EASY CHALLENGE
class Dog:
    def __init__(self):
        self.name = "Buddy"
my_dog = Dog()
print(my_dog.name)

# MEDIUM CHALLENGE
class Phone:
    def __init__(self):
        self.brand = "Samsung"
        self.battery = 100
phone = Phone()
print(phone.brand)
print(phone.battery)

# DIFFICULT CHALLENGE:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course = "Python"

student1 = Student("Alex", 15)
student2 = Student("John", 16)
print(student1.name, student1.age, student1.course)
print(student2.name, student2.age, student2.course)

# BONUS CHALLENGE:
class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
account = BankAccount("Alex")

account.deposit(100)
account.deposit(50)

print(account.owner)
print(account.balance)