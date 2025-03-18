# def say_hello(username, language="SW"):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     elif language == "RU":
#         print("Previet "+username)
#     elif language == "HE":
#         print("Shalom "+username)
#     elif language == "SW":
#         print("Jambo "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello('Liudmilla')
# say_hello('Reuben', 'HE')
# say_hello('Mikhail')
# say_hello('Daniel')

# fav_number = 12

# def my_func():
#     print("I put the func in function")
#     my_name = "george"
#     print(my_name)
#     print(fav_number)

# my_func()

# print(my_name)

# def number_multiplier(a):
#     return 17 * a

# new_num = number_multiplier(9)


# print(new_num)

# def format_name(first_name, last_name):
#     return (first_name.capitalize(), last_name.title())

# first, last = format_name("RICk", "mORTY")
# print(first)
# print(last)


# Write a function calculation() such that it can accept two 
# arguments and calculate the addition and subtraction of it. 
# And also it must return both addition and subtraction in a single return call

# def calculation(a,b):
#     return a+b, a-b

# x,y = calculation(40, 10)
# print(y)


# def greet_users(users):             # users should be a list
#     for user in users:              # Because it's a list, we can loop through it
#         print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

# # usernames = ["steve", "stan", "debbie"]
# # greet_users(usernames)

# dir(greet_users)


# def args_processer(*args):
#     for i in args:
#         print(i**2)

# args_processer(90,44)

# def kwargs_processor(**kwargs):
#     print(kwargs)

# kwargs_processor(teacher="aaron", student="markus")

# def sample(name, age, *args, **kwargs):
#     print(f"{name} went to the park. He is  {age}")
#     print(args)
#     print(kwargs)

# sample("Brutus", 55, "charlie", "Cuthburt", location="Ramat Gan", writing_utensil = "pencil")

# def check(a, b, c):
#     print(a, b, c)

# a = [1,2,3]
# check(*a)

# def upper_string(s):
#     return s.upper()

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(upper_string, fruit)

# print(list(map_object))
# print(fruit)

# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filtered_object = filter(starts_with_A, fruit)
# print(list(filtered_object))

# from functools import reduce

# def power_nums(first, second):
#     return first**second

# my_list = [1, 3, 5, 7, 9]
# reduced_list = reduce(power_nums, my_list)

# print(reduced_list)


# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

# map_object = map(lambda s: s.upper(), fruit)

# print(list(map_object))


# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

# filtered_object = filter(lambda s: s[0] == "A", fruit)

# print(list(filtered_object))

# def my_func(name, age, sunglasses):
#     print(f"my name is {name}. My age is {age}. I like wearing {sunglasses}")

# my_func("Aaron", 455, True)

# my = lambda name, age, sunglasses: f"my name is {name}. My age is {age}. I like wearing {sunglasses}"

# res = my('Aaron', 455, True)
# print(res)


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

short_names = filter(lambda name: len(name)<=4, people )
display_names = map(lambda name: f"hello {name}!!!", short_names)

for greeting in list(display_names):
    print(greeting)