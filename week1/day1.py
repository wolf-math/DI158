# print(type("45"))

# print(45 + 5)

# print("Hello Data People".replace("Data", "Full Stack"))

# Working with the following string:

# description = "strings are..."

# make it all uper case
# replace the word "are" to "is"
# print just the word "strings"

# print(description.upper())
# print(description.replace("are", "is"))
# print(description.replace(" are...", ""))

# my_age = 96
# print(my_age + 123978)

# bank_balance = '33000'
# phone_number = 532287514

# print(type(bank_balance))
# print(type(phone_number))

# print(int(bank_balance))
# print(str(phone_number))

# first_name = "Aaron"
# last_name = "Wolf"

# print(first_name, last_name)

# Given the following values:

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

# 1. Check if x is less than y and y is greater than z.

# 2. Verify if word1 is not equal to word2.

# 3. Use the bool() function to check the boolean value of z and word1.

# print(x<y and y>z) # True
# print(word1 != word2)
# print(bool(z), bool(word1))

# print1 = "hello"
# print(print1)


# You have a friend named Alice, and you want to send her a message with the following details:

# Name: Alice

# Age: 30

# City: New York

# Tasks:

# Use f-strings to print a message saying:

# "Hello, Alice! You are 30 years old and live in New York."

# name = "Alice"
# age = 30
# city = "New York"

# print(f"Hello, {name}! You are {age} years old and live in {city}.")

# next_week = input("What do you want to do next week? ")
# print(f"You want to {next_week} next week.")

# age = int(input("How old are you? "))
# print(f"Next year you will be {age + 1} years old")

# my_height = int(input("How tall are you? "))

# # if my_height > 200:
# #     print("You are too tall to ride!")
# # elif my_height < 150:
# #     print("You're too short!")
# # else:
# #     print("enjoy the ride")

# if my_height < 150 or my_height > 200:
#     print("You're not in the correct height range")
# else:
#     print("Enjoy the ride")

user_num = int(input("Choose a number between 1 and 100 "))

if user_num % 15 == 0:
    print("fizzbuzz")
elif user_num % 3 == 0:
    print("fizz")
elif user_num % 5 == 0:
    print("buzz")
else:
    print(user_num)