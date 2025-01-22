# ITP Week 2 Day 4 Exercise

# 1. Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 0
}

# SCENARIO: A person came in and bought one of everything!

# for item in inventory:
    # decrement item by using an assignment operator

    # NOTE: recall that item represents the key of the key:value pair

for item in inventory:
    inventory[item] -= 1


# 2. Implicit Functions 
# (When we work with global variables/objects and don't return anything, 
# these functions are implicit return functions!)

    # a. Dictionaries - create a function that takes in a dictionary which updates the "role" key value pair and makes it uppercase

def upper_role(person):
    person["role"] = person["role"].upper()



user_1 = {
    "firstName": "Stephanie",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "95485"
}
upper_role(user_1)



user_2 = {
    "firstName": "Brion",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "67344"
}

upper_role(user_2)




user_3 = {
    "firstName": "Daniel",
    "lastName": "Kim",
    "role": "Instructor",
    "id": "74324"
}

upper_role(user_3)
    # b. Dictionaries - Run the functions (3 times for each user!)


instructor_list = [user_1, user_2, user_3]
# print(instructor_list)

print(instructor_list)


    # c. List - create a function that takes in the list and 
    # checks if the each user's role is equal to "INSTRUCTOR". 
    # if it is the same, print VALID else print INVALID (try to use a loop here!)

def role_check(instructor_list):
    for user in instructor_list:
        if user["role"] == "INSTRUCTOR":
            print("VALID")
        else:
            print("INVALID")


    # d. List - Run the function with the instructor_list

print(role_check(instructor_list))

# role_check(instructor_list)

    # d. import the random module and update the function to re-assign the id of each user

    # e. don't forget to run it!
    
import random

def random_id(instructor_list):
    for user in instructor_list:
        user["id"] = random.randint(10000, 99999)
    return instructor_list


random_inst_list = random_id(instructor_list)
print(random_inst_list)


# 3. Explicit Functions

user_info = [46453, "Devin", "Smith"]
# Each element by index of user_info follows the format of: id, first_name, last_name

# Create a function with a parameter user_list
#   - return a dictionary with the following key-value pairs:
#   - id: user_list[0]
#   - first_name: user_list[1]
#   - last_name: user_list[2]

def user_to_dict(user_list):
    return {
        "id": user_list[0],
        "first_name": user_list[1],
        "last_name": user_list[2]
    }

# Calling the function and printing the result
print(user_to_dict(user_info))

