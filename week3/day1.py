# class Dog:
#     def __init__(self, name, color, sound):
#         # print("The dog has been initialized.")
#         self.name = name
#         self.color = color
#         self.sound = sound

#     def speak(self):
#         print(f"{self.name} says {self.sound}")

#     def walk(self, number_of_meters):
#         print(f"{self.name} walked {number_of_meters} meters")

#     def aged(self):
#         self.color = 'grey'




# my_dog = Dog('Peanut', 'Dark Brown', "quack")
# laras_dog = Dog('Mizette', 'Blue', "bark")

# # my_dog.speak()
# # laras_dog.speak()

# # my_dog.walk(1500)
# # laras_dog.walk(1200)

# print(my_dog.color)
# my_dog.aged()
# print(my_dog.color)




# Analyse the code below. What will be the ouput ?
# Explain the goal of the __init__() method

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)


# Analyse the code below. What will be the output ?
# Explain the goal of the methods
# Create a method that modifies the name of the person

# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

#   def change_name(self, new_name):
#     self.name = new_name

# first_person = Person("John", 36)
# first_person.show_details()

# first_person.change_name("Anania")
# first_person.show_details()


# class Computer():
#     # def __init__(self, brand):
#     #     self.brand = brand

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self.brand)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# mac_computer.is_garbage = False
# print(mac_computer.brand)

# dell_computer = Computer()
# dell_computer.brand = "Dell"

# print(dell_computer.brand)

# Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")

# # print(dell_computer.name)

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"greetings {self.name}")

    def street_greet(self):
        print(f"hey {self.nickname}")


# anna = Person('Anna')
# anna.greet()

# anna.nickname = 'An'
# anna.street_greet()

# anna.nickname = 'D Systems'
# anna.street_greet()


# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#         self.transactions = []

#     def view_balance(self):
#         self.transactions.append("View Balance")
#         print(f"Balance for account {self.account_number}: {self.balance}")

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount < 100:
#             print("Minimum deposit is 100")
#         else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw: {amount}")
#             print("Withdraw Approved")
#             return amount

#     def view_transactions(self):
#         print("Transactions:")
#         print("-------------")
#         for transaction in self.transactions:
#             print(transaction)


# aaronAcct = BankAccount(1, 100)
# markusAcct = BankAccount(2, 950000)

# aaronAcct.withdraw(150)
# markusAcct.withdraw(2000)

# aaronAcct.deposit(100)
# markusAcct.deposit(20000)

# aaronAcct.view_transactions()
# markusAcct.view_transactions()




