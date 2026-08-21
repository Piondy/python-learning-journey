score = int(input("Enter your score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 70:
    print("Grade: A\nExcellent!")
elif score >= 60:
    print("Grade: B\nVery Good!")
elif score >= 50:
    print("Grade: C\nGood")
elif score >= 45:
    print("Grade: D\nYou can do better.")
elif score >= 40:
    print("Grade: E\nKeep practicing.")
else:
    print("Grade: F\nYou need to improve")