# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

user_string = ''
while len(user_string) != 10:
    user_string = input("type a 10 char long string: ")
    if len(user_string) < 10:
        print("string not long enough")
    elif len(user_string) > 10:
        print("string too long")
    else:
        print("perfect string!")

# Then, print the first and last characters of the given text.
# The user enters "HelloWorld"
# Then you have to print 
# H
# d

print(user_string[0])
print(user_string[-1])

# 3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld

print_val = ''
for i in user_string:
    print_val += i
    print(print_val)

for i in range(len(user_string)):
	print(user_string[:i+1])

# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod
import random

for i in range(10):
    user_list = list(user_string)
    random.shuffle(user_list)
    # print(user_list)
    print(''.join(user_list))
