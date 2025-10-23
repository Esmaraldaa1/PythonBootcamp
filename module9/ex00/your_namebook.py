#!/usr/bin/python3

# key = firstname
# value = lastname

def array_of_names(names_dictionary):
    full_names = []

    # loop over all the first and last names and capitalize the first ltter
    for first_name, last_name in names_dictionary.items():
            first_name = first_name.capitalize()
            last_name = last_name.capitalize()

            full_names.append(f"{first_name} {last_name}")
            
    return full_names
            
# make the dictionary with persons names   
persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }

array_of_names(persons)
print(array_of_names(persons))