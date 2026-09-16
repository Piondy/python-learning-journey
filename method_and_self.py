# EASY CHALLENGE:
class Dog:
    def bark(self):
        print("Woof! Woof!")
my_dog = Dog()
my_dog.bark()

# MEDIUM CHALLENGE:
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1
        print(self.count)
counter = Counter()
counter.increase()
counter.increase()
counter.increase()
print(counter.count)

# DIFFICULT CHALLENGE:
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance -= amount

account = BankAccount()

account.deposit(100)
account.withdraw(30)
print(account.balance)

# BONUS CHALLENGE:
class Cup:
    def __init__(self):
        self.capacity = 12
        self.ounces = 0

    def fill(self, amount):
        if self.ounces + amount > self.capacity:
            print("Cup is full")
        else:
            self.ounces += amount
cup = Cup()

cup.fill(8)
cup.fill(3)

print(cup.ounces)