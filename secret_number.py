secret_number = 7
guess = int(input("Guess the number: "))
if guess == secret_number:
    print("🎉 Correct! You guessed the number!")
elif guess > secret_number:
    print("📈 Too high!")
else:
    print("📉 Too low!")