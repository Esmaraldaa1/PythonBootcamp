#!/usr/bin/python3

import sys

num_parameters = len(sys.argv) - 1

if num_parameters != 1:
    print('none')
else:
    print(sys.argv[1].upper())