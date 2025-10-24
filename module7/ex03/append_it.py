#!/usr/bin/python3

import sys

num_parameters = len(sys.argv) - 1

if num_parameters == 0:
    print("none")
else:
    parameters = sys.argv[1:] # : makes a list of all parameters, this says everything after index 0
    printed = False
    
    for parameter in parameters:
        positive = parameter.find("ism")
        if positive == len(parameter) - 3:
            continue
        else:
            print(parameter + "ism")
            printed = True
            
            if not printed:
                print("none")