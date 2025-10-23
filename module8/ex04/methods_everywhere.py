#!/usr/bin/python3
import sys

def shrink(string1):
    if not isinstance(string1, str):
        print("error, not a string")
    else:
        print(string1[:8]) #print the first 8 characters



def enlarge(string2):
    if not isinstance(string2, str):
        print("error, not a string")
    else:
        # if the lenght is < than 8, fill with 'z' untill 8
        while len(string2) < 8:
            string2 += "Z"
        print(string2)



def process_strings(argument):
    if not isinstance(argument, str):
        print("error, not a string")
        
    elif len(argument) > 8: #more than eight characters, call shrink
        shrink(argument)
    
    elif len(argument) < 8: #less than eight characters, call the enlarge
        enlarge(argument)
    else:
        print(argument)


# main program
arguments = sys.argv[1:]
if len(arguments) == 0:
    print("none")
else:
    for argument in arguments:
        process_strings(argument)
