#!/usr/bin/python3

age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")

for years in (10, 20, 30):
    print(f"In {years} years, you will be {age + years}.")