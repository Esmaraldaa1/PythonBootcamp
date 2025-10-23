#!/usr/bin/python3

import sys

num_parameters = len(sys.argv) - 1

if num_parameters == 0:
    print("none")
else:
    print(f"parameters: {num_parameters}")

    # get the parameters - the filename
    parameters = sys.argv[1:]

    # count the parameters and the lenght of them
    for param in parameters:
        print(f"{param} {len(param)}")