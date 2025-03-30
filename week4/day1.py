# with open('output.txt', 'w') as f:
#     for i in range(10):
#        f.write(f"this is line: {i}\n")

# Read the file line by line
# with open('names.txt', 'r') as f:
#     for i in f.readlines():
#         print(i)

# Read only the 5th line of the file
# with open('names.txt', 'r') as f:
#     print(f.readlines(5))

# # Read only the 5 first characters of the file
# with open('names.txt', 'r') as f:
#     text = f.read()[0:5]
#     print(text)

# Read all the file and return it as a list of strings. Then split each word
# skip for now

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# sw = {'Darth': 0, "Luke": 0, "Lea": 0}

# with open('names.txt', 'r') as f:
#     for i in f.readlines():
#         sw[i.rstrip()] += 1

# print(sw)

# Append your first name at the end of the file

# with open('names.txt', 'a') as f:
#     f.write('\nAaron')


# Append "SkyWalker" next to each first name "Luke"
# new_names = []
# with open('names.txt', 'r+') as f:
#     names = f.readlines()
#     for name in names:
#         # print(name)
#         if name.rstrip() == 'Luke':
#             new_names.append("Luke Skywalker\n")
#         else:
#             new_names.append(name)

#     for name in new_names:
#         f.write(name)


# import json

# my_family = {
#     "grandparent": ["Rick"],
#     "parents":['Beth', 'Jerry'],
#     "children":['Summer', 'Morty']
# }

# with open("my_fam.json", 'w') as file_obj:
#     json.dump(my_family, file_obj, indent = 2, sort_keys=True)

import requests

# current_location = requests.get("http://api.open-notify.org/iss-now.json")

# current_json = current_location.json()

# print(current_json['iss_position'])


# Use the Chuck Norris API https://api.chucknorris.io/ to retrieve some jokes in a specific category
# Use every notion described in the lesson

chuck_url = "https://api.chucknorris.io/jokes/random?category=dev"

req = requests.get(chuck_url)

info = req.json()

joke = info['value']

print(joke)