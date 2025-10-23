#!/usr/bin/python3

import sys

num_parameters = len(sys.argv) - 1

if num_parameters < 2:
    print("none")
else:
    parameters = sys.argv[1:]
    reversed_params = parameters[::-1] # slice to reverse order 
    
    print(" ".join(reversed_params)) # put them together again