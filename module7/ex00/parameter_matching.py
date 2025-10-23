#!/usr/bin/python3

import sys

num_parameters = len(sys.argv) - 1

if num_parameters != 1:
    print("none")
else:
   expected_word = sys.argv[1]

user_input = input(f"Enter the word '{expected_word}': ")

if user_input == expected_word:
    print("Good job!")
else:
    print("Nope, sorry...")