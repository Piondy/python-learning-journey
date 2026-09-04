user_input1 = input("Enter the number of bananas: ")
if user_input1.isdigit():
    bananas = int(user_input1)
    user_input2 = input("Enter the number of milk: ")
    if user_input2.isdigit():
        milk = float(user_input2)
        total = bananas + milk
        print(f"You entered {user_input1} bananas and {user_input2} milks.\nTotal ingredients: {total}")
    else:
        print("Invalid input! Please enter a number.")
else:
    print("Invalid input! Please enter a number.")