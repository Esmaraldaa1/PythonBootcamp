#!/usr/bin/python3

# key = name
# value = haircolor

def find_the_redheads(family_dictionary):
    red_heads = list(filter(
        lambda name_color: name_color[1] == 'red', 
        family_dictionary.items()
        ))
    
    names = []
    for item in red_heads:
        names.append(item[0])
    return names

# make the dictionary with persons and haircolor  
dupont_family = {
    "florian" : "red",
    "marie" : "blond",
    "virginie": "brunette",
    "david" : "red",
    "franck" : "red"
}

find_the_redheads(dupont_family)
print(find_the_redheads(dupont_family))