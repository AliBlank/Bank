# class Person:
#     def __init__(self, name, age, gender):   # "self" Object Ro Barmigardone
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# def show_profile(person):
#     return f'Profile: {person.name} {person.age} {person.gender} '
#
#
# person1 = Person('ali', 20, 'male')
# print(show_profile(person1))
#
# ----------------------------------------------------------------------------------------------
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # def show(self):
#     #     return f'{self.name} is {self.age} years old'
#
#     def __repr__(self):
#         return f'{self.name} is {self.age} years old'
#
#
# person1 = Person('ali', 20)
#
# print(person1)
#
# -----------------------------------------------------------------------------
#
# class Person:
#     car = 1
#     count_profile = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.count_profile += 1
#
#     def __repr__(self):
#         return f'Person({self.name}, {self.age})'
#
#
#
# person1 = Person('John', 20)
# person2 = Person('John', 23)
# person3 = Person('John', 24)
# print(person1)
# print(person2)
# print(person3)
# print(person1.count_profile)
# print(Person.__dict__)
# print(person1.__dict__)
#
# ------------------------------------------------
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def input_profile(cls,input_text):
#         name,age = input_text.split(' ')
#         return cls(name,age)
#
#     def __str__(self):
#         return f'Your name is {self.name} and your age is {self.age}'
#
#     @staticmethod
#     def say_hello():
#         print('Hello World!')
#
# # information = input('Enter Your Name And Age:')
#
# # person = Person.input_profile(information)
# # print(person)
# print(Person.say_hello())
#
# --------------------------------------------------------------------------------------
#
#
# class User:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def email(self):
#         return f'{self.fname}.{self.lname}@gmail.com'
#
#     def __repr__(self):
#         return f'User : ({self.fname}, {self.lname}) | User Email: {self.email()}'
#
#
#
# class Developer(User):
#     def __init__(self, fname, lname,salary,position):
#         super().__init__(fname, lname)
#         self.salary = salary
#         self.position = position
#
#     def email(self):
#         return f'{self.lname}.{self.fname}@gmail.com'
#
#     def __repr__(self):
#         return f'Developer : ({self.fname} {self.lname}) Devloper Salary : {self.salary} | Developer Position : {self.position} | Developer Email: {self.email()}'
#
#
#
#
# User1 = User('mamad','moradi')
# print(User1)
# print('-'*50)
# Dev = Developer('ali','souri',20000,1)
# print(Dev)
#
# ---------------------------------------------------------------------------------------------------------
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__salary = 20000
#         self.__password = '270186'
#
#     def get_salary(self):
#
#         passcode =input('Enter your password to show salary: ')
#
#         if passcode == self.__password:
#             return f'Your salary is {self.__salary}'
#         else:
#             return f'Wrong Password'
#
#     def __str__(self):
#         return f'Name: {self.name}\nAge: {self.age}'
#
#
#
# person1 = Person('John', 24)
# print(person1)
#
# print(person1.get_salary())
#
#
# -----------------------------------------------------------------------------------------
#
# class Car:
#     car_wheel = 4
#     def __init__(self, name, maxspeed, kmage):
#         self.name = name
#         self.maxspeed = maxspeed
#         self.kmage = kmage
#
#
#     def passengers(self, max_passengers=5):
#         return f'{self.name} Max Passenger Is {max_passengers}'
#
#
#     def __str__(self):
#         return f'CarName: {self.name}\nMaxspeed : {self.maxspeed}\nKmage : {self.kmage}'
#
#
# class Bus(Car):
#
#     def passengers(self, max_passengers=17):
#         return super().passengers(max_passengers)
#
#     def __str__(self):
#         return f'Bus Name:{self.name}\nMaxspeed : {self.maxspeed}\nKmage : {self.kmage}'
#
#
#
#
# BMW = Car('BMW', 200, 100)
# print(BMW)
# print('-'*50)
# Bus = Bus('BENZ', 130, 100)
# print(Bus)
# print('-'*50)
# print(BMW.passengers())
# print('-'*50)
# print(Bus.passengers())
# print('-'*50)
# print(f'Car And Bus Have {Car.car_wheel} Wheels')
#

#------------------------------------------------------------------------------

# def upper(text):
#     return text.upper()
#
#
# def lower(text):
#     return text.lower()
#
#
# print(lower('hello world'))

#---------------------------------------------------------------------------

# def plus(x):
#     def add(y):
#         return x + y
#     return add
#
#
# num1 = plus(3)
# print(num1(10))

#-----------------------------------------------------------------------------

# def style(func):
#     def wrapper(*args,):
#         print('*'*20)
#         func(*args)
#         print('*'*20)
#     return wrapper
#
# @style
# def main():
#     print('Alisouri')
#
# main()
#
# @style
# def greet(name):
#     print(f'Hello {name}')
#
# greet('Alisouri')
#
# @style
# def full_name(name,age,gender):
#     print(f'Hello {name} {age} {gender}')
#
# full_name('Alisouri',22,'M')

#-------------------------------------------------------------

# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# my_map = map(lambda x: x*2, my_list)
# for item in my_map:
#     print(item)
# my_filter = filter(lambda x: x%2==0, my_list)
# for j in my_filter:
#     print(j)

#-----------------------------------------------------------------

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]
#
# for item in zip(list1, list2, list3):
#     print(item)
#

#------------------------------------------------------------------
#
# my_list = [i for i in range(10) if i % 2 == 0]
# print(my_list)

#-----------------------------------------------------------------

# import random
# import string
#
# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password
#
# # طول پسورد دلخواه را تعیین کنید
# password_length = 40
# password = generate_password(password_length)
# print(f"پسورد شما: {password}")

