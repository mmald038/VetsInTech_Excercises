import json 


example_dict = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ["Ann", "Billy"],
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

example_json = json.dumps(example_dict)  # converts a Python object into a JSON string

#print(example_json)


# print the indented JSON
indented_json = json.dumps(example_dict, indent=4)
 

#print(indented_json)

# print the separated and indented JSON
separated_indented_json = json.dumps(example_dict, indent=4, separators=(". ", "= "))
 

#print(separated_indented_json)

# print the sorted and indented JSON and sort the keys alphabetically

sorted_indented_json = json.dumps(example_dict, indent=4, sort_keys=True)
 

#print(sorted_indented_json)