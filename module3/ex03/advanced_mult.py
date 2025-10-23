#!/usr/bin/python3

# Start with table 0
table_number = 0

# Outer while-loop: go through each multiplication table (0 to 10)
while table_number <= 10:
    print(f"Table of {table_number}:", end=" ")

    # Inner while-loop: multiply by numbers 0 to 10
    multiplier = 0
    while multiplier <= 10:
        print(table_number * multiplier, end=" ")
        multiplier += 1

    print()  # Move to the next line after one table
    table_number += 1