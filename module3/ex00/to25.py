#!/usr/bin/python3

number = int(input("Enter a number less than 25: "))

if number > 25:
    print('Error')

while number <= 25:  
# Increment the value of the variable "number by 1"
    print('Inside the loop, my variable is', number)
    number = number + 1