#!/usr/bin/python3

originalArray = [2, 8, 9, 48, 8, 22, -12, 2]

newArray = [number + 2
            for number in originalArray
            if number > 5]

print(originalArray)
print(set(dict.fromkeys(newArray))) #dict = object