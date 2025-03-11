# fewd = ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']

# sorted_fewd = sorted(fewd)

# print(sorted_fewd)


# x = fruits.index("cherry")
    
# list1 = [5, 10, 15, 20, 25, 50, 20]

# twenty_index = list1.index(20)

# print(twenty_index) # 3

# list1[twenty_index] = 200

# print(list1)

# Unpack the following tuple into 4 variables

# Expected output:

# a_tuple = (10, 20, 30, 40)

# a = a_tuple[0]
# b = a_tuple[1]
# c = a_tuple[2]
# d = a_tuple[3]

# # Your code
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print 30
# print(d) # should print 40

# cities = ["London", "San Francisco", "Paris", "Barcelona"]

# for llama in cities:
#     print("I once went to", llama)

# for num in range(0,11,2):
#     print(num)

# sum_this_list = [1,2,3,4,5]

# print(sum(sum_this_list))

# total = 0
# for i in sum_this_list:
#     total += i

# print(total)

# Accept a number from the user and print its multiplication table

# user_num = int(input("Pick a number for mult table"))
# for number in range(11):
#     print(f"{number} x {user_num} = {user_num * number}")


# a_number = 1

# while a_number < 12:
#     print(a_number)
#     a_number += 1


# password = ''
# while password != 'hello-world-123':
#   password = input('What is the top secret password? ')

# print('You guessed the right password!')

# t = 1
# while t<=10:
#     print(t)
#     t+=1

# while True: 
#     city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if city == 'quit':
#         break
#     elif city == 'leave me alone':
#         break
#     elif city == 'stop':
#         break
#     else:
#         print("I'd love to go to", city)

# print("Goodbye !")

g = 0
while g < 12:
    g+=1
    
    if g == 7:
        continue

    print(g)
