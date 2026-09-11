def calculate_price(quantity, price):
    total = quantity * price
    return total
print(calculate_price(4, 5))

def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
check_number(-5)