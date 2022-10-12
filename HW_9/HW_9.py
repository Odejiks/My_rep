from dataclasses import dataclass


# Task 1
# @dataclass
# class Auto:
#     """vehicle dataclass"""
#
#     mark: str
#     model: str
#     age: int
#     color: str
#     price: int
#
#
# class Car:
#
#     """this is a car class"""
#
#     def __init__(self, auto):
#         self.auto = auto
#
#     def my_auto(self):
#         print(f"mark: {self.auto.mark}"'\n'
#               f"model: {self.auto.model}"'\n'
#               f"color: {self.auto.color}"'\n'
#               f"age: {self.auto.age}"'\n'
#               f"price: {self.auto.price}"'\n'
#               )
#
#
# auto_1 = Auto(mark='kia',
#               model='ceed',
#               age=2013,
#               color='green',
#               price=2000)
#
# auto_2 = Auto(mark='opel',
#               model='astra',
#               age=2016,
#               color='black',
#               price=5000)
#
# car_1 = Car(auto_1)
# car_1.my_auto()
#
# car_2 = Car(auto_2)
# car_2.my_auto()


# # Task 2-3
#
# """create a class User"""
#
#
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     """use method Info"""
#     def Info(self):
#         print(f"{self.name} - {self.email}")
#
#     """create a classmethod"""
#     @classmethod
#     def get_Info(cls, date):
#         name, email = date
#         return cls(name, email)
#
#     """create a staticmethod"""
#     @staticmethod
#     def get_Info_sta(self):
#         print(f"{self.name} - {self.email}")
#
#
# user = ("Petrov", "pet@per.com")
#
# user_1 = User.get_Info(user)
# user_1.Info()
# user_1.get_Info_sta(user_1)
