#!/usr/bin/python3

import sys
import re

num_parameters = len(sys.argv) - 1

if num_parameters != 2:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    matches = re.findall(keyword, text)

    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))