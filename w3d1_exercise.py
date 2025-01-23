# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]

[{"user_id1":0, "name": "Alex"}, {"user_id2":1, "name": "Bob"}, {"user_id3":2, "name": "Charlie"}, {"user_id4":3, "name": "Dexter"}, {"user_id5":4, "name": "Edgar"}, {"user_id6":5, "name": "Frank"}, {"user_id7":6, "name": "Gary"}]

# 1a. Create a function that takes a single string value and returns the desired dictionary

def string_to_dict(string):
    return {"user_id": users_list.index(string), "name": string}

print(string_to_dict("Charlie"))          # {"user_id": 2, "name": "Charlie"}


# 1b. Create a new empty list called users_dict_list

user_dict_list = []

# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list

for index, user in enumerate(users_list):
    user_dict_list.append({"user_id": index, "name": user})

print(user_dict_list)     # [{"user_id": 0, "name": "Alex"}, {"user_id": 1, "name": "Bob"}, etc, etc]

# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?

from w3d1_mock_data import mock_data

# 2a. retrieve the gender of Morty Smith

print(mock_data["results"][1]["gender"])      # "Male"

# 2b. retrieve the length of the Rick Sanchez episodes

print(len(mock_data["results"][0]["episode"]))    # 51



# 2c. retrieve the url of Summer Smith location


print(mock_data["results"][2]["location"]["url"])    # "https://test-rick_and_morty.com/location/20"




"""
 THIS IS THE MOCK DATA FOR RICK AND MORTY API

mock_data = {
  "info": {
    "count": 826,
    "pages": 42,
    "next": "https://test-rick_and_morty.com/character/?page=2",
    "prev": None
  },
  "results": [
    {
      "id": 1,
      "name": "Rick Sanchez",
      "status": "Alive",
      "species": "Human",
      "type": "",
      "gender": "Male",
      "origin": {
        "name": "Earth (C-137)",
        "url": "https://test-rick_and_morty.com/location/1"
      },
      "location": {
        "name": "Citadel of Ricks",
        "url": "https://test-rick_and_morty.com/location/3"
      },
      "image": "https://test-rick_and_morty.com/character/avatar/1.jpeg",
      "episode": [
        "https://test-rick_and_morty.com/episode/1",
        "https://test-rick_and_morty.com/episode/2",
        "https://test-rick_and_morty.com/episode/3",
        "https://test-rick_and_morty.com/episode/4",
        "https://test-rick_and_morty.com/episode/5",
        "https://test-rick_and_morty.com/episode/6",
        "https://test-rick_and_morty.com/episode/7",
        "https://test-rick_and_morty.com/episode/8",
        "https://test-rick_and_morty.com/episode/9",
        "https://test-rick_and_morty.com/episode/10",
        "https://test-rick_and_morty.com/episode/11",
        "https://test-rick_and_morty.com/episode/12",
        "https://test-rick_and_morty.com/episode/13",
        "https://test-rick_and_morty.com/episode/14",
        "https://test-rick_and_morty.com/episode/15",
        "https://test-rick_and_morty.com/episode/16",
        "https://test-rick_and_morty.com/episode/17",
        "https://test-rick_and_morty.com/episode/18",
        "https://test-rick_and_morty.com/episode/19",
        "https://test-rick_and_morty.com/episode/20",
        "https://test-rick_and_morty.com/episode/21",
        "https://test-rick_and_morty.com/episode/22",
        "https://test-rick_and_morty.com/episode/23",
        "https://test-rick_and_morty.com/episode/24",
        "https://test-rick_and_morty.com/episode/25",
        "https://test-rick_and_morty.com/episode/26",
        "https://test-rick_and_morty.com/episode/27",
        "https://test-rick_and_morty.com/episode/28",
        "https://test-rick_and_morty.com/episode/29",
        "https://test-rick_and_morty.com/episode/30",
        "https://test-rick_and_morty.com/episode/31",
        "https://test-rick_and_morty.com/episode/32",
        "https://test-rick_and_morty.com/episode/33",
        "https://test-rick_and_morty.com/episode/34",
        "https://test-rick_and_morty.com/episode/35",
        "https://test-rick_and_morty.com/episode/36",
        "https://test-rick_and_morty.com/episode/37",
        "https://test-rick_and_morty.com/episode/38",
        "https://test-rick_and_morty.com/episode/39",
        "https://test-rick_and_morty.com/episode/40",
        "https://test-rick_and_morty.com/episode/41",
        "https://test-rick_and_morty.com/episode/42",
        "https://test-rick_and_morty.com/episode/43",
        "https://test-rick_and_morty.com/episode/44",
        "https://test-rick_and_morty.com/episode/45",
        "https://test-rick_and_morty.com/episode/46",
        "https://test-rick_and_morty.com/episode/47",
        "https://test-rick_and_morty.com/episode/48",
        "https://test-rick_and_morty.com/episode/49",
        "https://test-rick_and_morty.com/episode/50",
        "https://test-rick_and_morty.com/episode/51"
      ],
      "url": "https://test-rick_and_morty.com/character/1",
      "created": "2017-11-04T18:48:46.250Z"
    },
    {
      "id": 2,
      "name": "Morty Smith",
      "status": "Alive",
      "species": "Human",
      "type": "",
      "gender": "Male",
      "origin": {
        "name": "unknown",
        "url": ""
      },
      "location": {
        "name": "Citadel of Ricks",
        "url": "https://test-rick_and_morty.com/location/3"
      },
      "image": "https://test-rick_and_morty.com/character/avatar/2.jpeg",
      "episode": [
        "https://test-rick_and_morty.com/episode/1",
        "https://test-rick_and_morty.com/episode/2",
        "https://test-rick_and_morty.com/episode/3",
        "https://test-rick_and_morty.com/episode/4",
        "https://test-rick_and_morty.com/episode/5",
        "https://test-rick_and_morty.com/episode/6",
        "https://test-rick_and_morty.com/episode/7",
        "https://test-rick_and_morty.com/episode/8",
        "https://test-rick_and_morty.com/episode/9",
        "https://test-rick_and_morty.com/episode/10",
        "https://test-rick_and_morty.com/episode/11",
        "https://test-rick_and_morty.com/episode/12",
        "https://test-rick_and_morty.com/episode/13",
        "https://test-rick_and_morty.com/episode/14",
        "https://test-rick_and_morty.com/episode/15",
        "https://test-rick_and_morty.com/episode/16",
        "https://test-rick_and_morty.com/episode/17",
        "https://test-rick_and_morty.com/episode/18",
        "https://test-rick_and_morty.com/episode/19",
        "https://test-rick_and_morty.com/episode/20",
        "https://test-rick_and_morty.com/episode/21",
        "https://test-rick_and_morty.com/episode/22",
        "https://test-rick_and_morty.com/episode/23",
        "https://test-rick_and_morty.com/episode/24",
        "https://test-rick_and_morty.com/episode/25",
        "https://test-rick_and_morty.com/episode/26",
        "https://test-rick_and_morty.com/episode/27",
        "https://test-rick_and_morty.com/episode/28",
        "https://test-rick_and_morty.com/episode/29",
        "https://test-rick_and_morty.com/episode/30",
        "https://test-rick_and_morty.com/episode/31",
        "https://test-rick_and_morty.com/episode/32",
        "https://test-rick_and_morty.com/episode/33",
        "https://test-rick_and_morty.com/episode/34",
        "https://test-rick_and_morty.com/episode/35",
        "https://test-rick_and_morty.com/episode/36",
        "https://test-rick_and_morty.com/episode/37",
        "https://test-rick_and_morty.com/episode/38",
        "https://test-rick_and_morty.com/episode/39",
        "https://test-rick_and_morty.com/episode/40",
        "https://test-rick_and_morty.com/episode/41",
        "https://test-rick_and_morty.com/episode/42",
        "https://test-rick_and_morty.com/episode/43",
        "https://test-rick_and_morty.com/episode/44",
        "https://test-rick_and_morty.com/episode/45",
        "https://test-rick_and_morty.com/episode/46",
        "https://test-rick_and_morty.com/episode/47",
        "https://test-rick_and_morty.com/episode/48",
        "https://test-rick_and_morty.com/episode/49",
        "https://test-rick_and_morty.com/episode/50",
        "https://test-rick_and_morty.com/episode/51"
      ],
      "url": "https://test-rick_and_morty.com/character/2",
      "created": "2017-11-04T18:50:21.651Z"
    },
    {
      "id": 3,
      "name": "Summer Smith",
      "status": "Alive",
      "species": "Human",
      "type": "",
      "gender": "Female",
      "origin": {
        "name": "Earth (Replacement Dimension)",
        "url": "https://test-rick_and_morty.com/location/20"
      },
      "location": {
        "name": "Earth (Replacement Dimension)",
        "url": "https://test-rick_and_morty.com/location/20"
      },
      "image": "https://test-rick_and_morty.com/character/avatar/3.jpeg",
      "episode": [
        "https://test-rick_and_morty.com/episode/6",
        "https://test-rick_and_morty.com/episode/7",
        "https://test-rick_and_morty.com/episode/8",
        "https://test-rick_and_morty.com/episode/9",
        "https://test-rick_and_morty.com/episode/10",
        "https://test-rick_and_morty.com/episode/11",
        "https://test-rick_and_morty.com/episode/12",
        "https://test-rick_and_morty.com/episode/14",
        "https://test-rick_and_morty.com/episode/15",
        "https://test-rick_and_morty.com/episode/16",
        "https://test-rick_and_morty.com/episode/17",
        "https://test-rick_and_morty.com/episode/18",
        "https://test-rick_and_morty.com/episode/19",
        "https://test-rick_and_morty.com/episode/20",
        "https://test-rick_and_morty.com/episode/21",
        "https://test-rick_and_morty.com/episode/22",
        "https://test-rick_and_morty.com/episode/23",
        "https://test-rick_and_morty.com/episode/24",
        "https://test-rick_and_morty.com/episode/25",
        "https://test-rick_and_morty.com/episode/26",
        "https://test-rick_and_morty.com/episode/27",
        "https://test-rick_and_morty.com/episode/29",
        "https://test-rick_and_morty.com/episode/30",
        "https://test-rick_and_morty.com/episode/31",
        "https://test-rick_and_morty.com/episode/32",
        "https://test-rick_and_morty.com/episode/33",
        "https://test-rick_and_morty.com/episode/34",
        "https://test-rick_and_morty.com/episode/35",
        "https://test-rick_and_morty.com/episode/36",
        "https://test-rick_and_morty.com/episode/38",
        "https://test-rick_and_morty.com/episode/39",
        "https://test-rick_and_morty.com/episode/40",
        "https://test-rick_and_morty.com/episode/41",
        "https://test-rick_and_morty.com/episode/42",
        "https://test-rick_and_morty.com/episode/43",
        "https://test-rick_and_morty.com/episode/44",
        "https://test-rick_and_morty.com/episode/45",
        "https://test-rick_and_morty.com/episode/46",
        "https://test-rick_and_morty.com/episode/47",
        "https://test-rick_and_morty.com/episode/48",
        "https://test-rick_and_morty.com/episode/49",
        "https://test-rick_and_morty.com/episode/51"
      ],
      "url": "https://test-rick_and_morty.com/character/3",
      "created": "2017-11-04T19:09:56.428Z"
    }
  ]
}


"""