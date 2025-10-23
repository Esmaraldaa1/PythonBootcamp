#!/usr/bin/python3

from decimal import Decimal

userInput = input("Give me a number: ")

number = Decimal(userInput) #convert string to decimal
42
if number == number.to_integral_value(): # examp: 42.00 to 42
    print("This number is a integer")
else:
    print("This number is a decimal")