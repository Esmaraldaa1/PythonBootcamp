#!/usr/bin/python3

import sys
import re

num_parameters = len(sys.argv) - 1

if num_parameters != 1:
    print("none")
else:
    text = sys.argv[1]

    # find all 'z's
    z_list = re.findall("z", text)

    # if there no 'z' is found
    if not z_list:
        print("none")
    else:
        # print all z's
        print("".join(z_list))
