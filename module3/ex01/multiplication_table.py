#!/usr/bin/python3

number = int(input("Enter a number: \n"))

for i in range(0, 10):
    result = number * i
    print(f"{i} x {number} = {result}")