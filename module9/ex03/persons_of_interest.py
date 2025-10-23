#!/usr/bin/python3

def famous_births(figures_dictionary):
    # Sort all scientists by their birth date (oldest to youngest)
    # .items() gives key/value pairs from the dictionary
    sorted_figures = sorted(
    figures_dictionary.items(),
    key=get_birth_date)

    # Loop through the sorted results and print the name + birth year in the right format
    for key, info in sorted_figures:
        print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")

def get_birth_date(item):
    return item[1]["date_of_birth"]

# Dictionary with historic figures
figures = {
    "lovelace": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "meitner": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "payne": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "hopper": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(figures)