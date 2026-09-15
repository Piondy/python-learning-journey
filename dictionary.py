student = {
    "name": "Alex",
    "age": 15,
    "course": "python"
}

print(student["name"])
print(student["age"])
print(student["course"])

menu = {
    "Burger": 5.00,
    "Pizza": 8.00,
    "Juice": 3.00
}

menu["Burger"] = 6.00
menu["Fries"] = 2.50

print(menu)

user = {
    "username": "alex123",
    "email": "alex@example.com",
    "age": 15
}

print(user["username"])
user["age"] = 16
user["country"] = "Nigeria"
print(user.get("phone", "Not provided"))
print(user)

drink = {
    "Latte": 4.50,
    "Espresso": 3.50,
    "Mocha": 5.00
}

ask = input("Enter a drink: ")
if ask in drink:
    drink.get(ask)
    print(drink[ask])
else:
    print("Drink not found")