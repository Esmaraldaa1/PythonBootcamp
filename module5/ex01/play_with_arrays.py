#!/usr/bin/python3

originalArray = [2, 8, 9, 48, 8, 22, -12, 2]

newArray = [numberInOldArray + 2 
            for numberInOldArray
            in originalArray
            ]
print(f"Original array: {originalArray}\nNew Array: {newArray} ")