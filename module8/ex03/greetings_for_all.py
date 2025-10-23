#!/usr/bin/python3

def greetings(name="noble stranger"):
    # checkt if parameter is a string
    if not isinstance(name, str):
        print("Error: It was not a name.")
    else:
        print(f"Welcome, {name}!")
        
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
