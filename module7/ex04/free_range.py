#!/usr/bin/python3

import sys

num_parameters = len(sys.argv) - 1

if num_parameters != 2:
    print("none")
else:
    try:
        start = int(sys.argv[1]) #parameter 1
        end = int(sys.argv[2])  #parameter 2
    except ValueError:
        print("none")
        sys.exit()

    # check of start < end
    if start >= end:
        print("none")
    else:
        # make the list with numbers between start and end
        numbers = list(range(start, end + 1))
        print(numbers)