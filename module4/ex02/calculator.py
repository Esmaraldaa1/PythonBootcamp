#!/usr/bin/python3

number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))
print('Thank you!')

# use dictionary (object) 
operators = { 
    "+": number1 + number2, 
    "-": number1 - number2, 
    "/": number1 // number2, 
    "*": number1 * number2 
    } 

for operator, result in operators.items(): 
    print(f"{number1} {operator} {number2} = {result}")