# This script let's you enter a year of your choice and then tell's you if it is a leap year or not

year = int(input("Which year do you want to check? "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Leap year.")
else:
    print(f"Not leap year")
