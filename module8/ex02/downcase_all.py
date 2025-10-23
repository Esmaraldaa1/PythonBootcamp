#!/usr/bin/python3
import sys

def downcase_it(parameter1,parameter2):
    word1 = parameter1.lower()
    word2 = parameter2.lower()

    print(word1 + "\n" + word2)

num_parameters = len(sys.argv) - 1

if num_parameters != 2:
    print("none")
else:
    parameter1 = sys.argv[1]
    parameter2 = sys.argv[2]
    downcase_it(parameter1, parameter2)