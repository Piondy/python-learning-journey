#EASY CHALLENGE:
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

#MEDIUM CHALLENGE:
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
new_num = [n for n in numbers1 if n > 4]
print(new_num)

#dIFFICULT CHALLENGE:
prices = {
    "Burger": 5.00,
    "Pizza": 8.00,
    "Juice": 3.00
}
new_prices = {new: price + 1 for new, price in prices.items()}
print(new_prices)

#BONUS CHALLENGE:
sizes = ["large", "small", "large", "medium", "small"]
new_sizes = ["Premium" if i == "large" else "Regular" for i in sizes]
print(new_sizes)
