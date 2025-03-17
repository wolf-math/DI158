# shirts = [
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   },
# ]

# print(shirts[1]['price'])

# Access the value of key history


# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict["class"]["student"]["marks"]["history"])


# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# print(a_dict.items())
# # output : 
# # dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

# # The items() method returns a view object that displays 
# # a list of dictionary's (key, value) tuple pairs.


# for key, value in a_dict.items():
#     print(key, '->', value)


# Delete set of keys from Python Dictionary


# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# keys_to_remove = ["name", "salary"]

# for key in keys_to_remove:
#     del sample_dict[key]

# # del sample_dict['name']
# # del sample_dict['salary']

# print(sample_dict)


# for i in range(1, 10):
#     print(i)
#     # if i == 9:
#     #     break
# # else:
# print('The for loop is over')


# for letter in 'Leonardo':
#     if letter == 'a':
#         pass
#     print(letter, end='')

# my_number = '1234'

# my_list = [int(num) * 2 for num in my_number]
# print(my_list)

# # same as:
# my_list = []
# for num in my_number:
#     my_list.append(int(num) * 2)

# print(my_list)

family_age = {'Lea': 12, 'Mark': 25, 'George': 50}

new_year = 1

new_family_age = {name: age+new_year for (name, age) in family_age.items()}

print(new_family_age)