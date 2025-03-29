class Israeli:
    prime_minister = "Bibi"
    num_citizens = 0

    def __init__(self, name):
        self.name = name
        Israeli.num_citizens += 1
        self.__tz = Israeli.num_citizens

    @property
    def get_tz(self):
        return f"{self.__tz} 7" 


# liudmila = Israeli("Liudmila")
# gabby = Israeli("gabby")
# hadriel = Israeli("hadriel")
# ilan = Israeli("ilan")
# other_ilan = Israeli("other_ilan")
# daniel = Israeli("daniel")

# # # other_ilan.get_tz()

# print(daniel.get_tz)
# daniel.__tz = 87

# print(daniel.__tz)

# daniel.get_tz()

# print(Israeli.prime_minister)

# hadriel = Israeli('Hadriel', 1)

# print(hadriel.name)
# print(hadriel.tz)
# print(hadriel.prime_minister)


# liudmila = Israeli("Liumila", 2)

# # print(liudmila.name)
# # print(liudmila.tz)
# print(liudmila.prime_minister)

# Israeli.prime_minister = "LeBron"

# print(liudmila.prime_minister)

# Analyse the code below. What will be the outputs ?

# Explain the goal of the methods

# class Circle:
#     color = "red"
#     color2 = "blue"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#        return Circle.color2

# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)


# class Man:
#     sex = "Male"

#     @staticmethod
#     def get_nicknames():
#         return ["Bro", "Dude", "Buddy"]
    
# alex = Man()

# print(alex.get_nicknames())


# class MyClass:
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print(f"Value of object : {object_1.get_val()}") # 10
# print(MyClass.get_count()) # 1

# object_2 = MyClass(20)
# print(f"Value of object : {object_2.get_val()}") # 20
# print(MyClass.get_count()) # 2


# class Ilan:
#     def __init__(self, coolness_level):
#         self.coolness_level = coolness_level

#     def __str__(self):
#         return f"This Ilan has a coolness value of {self.coolness_level}"
    
#     def __len__(self):
#         return self.coolness_level
    
#     def __call__(self):
#         for i in range(self.coolness_level):
#             print(f"I'm cool {i + 1} times")

#     def __add__(self, *args):
#          self.coolness_level += sum(args)
#          print("coolness level updated")
#          return self.coolness_level
    
#     def __iadd__(self):
#         pass

# # ilans = Ilan(8)

# # # print(ilans)

# # # print(len(ilans))

# # # ilans()

# # ilans + 5

# # ilans()

# print(dir(Ilan))

# class Person:
#     def __init__(self, name, lastName):
#         self.name = name
#         self.lastName = lastName


# #Here we overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'

#     def __repr__(self):

#     # We can write whatever we want inside this method, but we have to return an object.

#         return f"{self.__class__.__name__} : {self.name} {self.lastName}"

#     def __add__(self,other):
#         name = self.name[0] + other.name[1:]
#         lastname = other.lastName
#         return Person(name,lastname)

# father = Person('John', 'Snow')
# mother = Person('Kaleesi', 'MotherOfDragons')
# # using the __add__() method
# dragonChild = father + mother 

# print(dragonChild)

# class PrintList:

#     def __init__(self, my_list):
#         self.mylist = my_list

#     def __repr__(self):
#         return str(self.mylist)


# printlist = PrintList(["a", "b", "c"])
# print(printlist)

# import math

# print(math.e)


# import time

# before = time.time()
# long_number = 1000**1000
# after = time.time()

# print(f"It took {after - before} seconds to execute 1000**1000")


import datetime

today_date = datetime.date.today()
actual_datetime = datetime.datetime.now()
in_15_hours = actual_datetime + datetime.timedelta(hours=-15, minutes=10)

print(f"Today is the {today_date.day}/{today_date.month}")
print(f"15 hours ago and 10 minutes it was be the {in_15_hours.day}/{in_15_hours.month}")


