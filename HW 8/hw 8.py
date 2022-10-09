import time


class auto:
    """creating a consumer class
   :param brand: car brand
   :param age: year of car manufacture
   :param mark: car model
   :param color: car color
   :param weight: vehicle weight
   """
    brand = ""
    age = 0
    color = ""
    mark = ""
    weight = 0

    def __init__(self, brand: str, age: int, mark: str):
        """required attribute method"""
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        """ deduce the move """
        print("move")

    def birthday(self):
        """ increase the age attribute by 1"""
        print(self.age + 1)

    @staticmethod
    def stop():
        """deduce stop"""
        print("stop")


class Truck(auto):
    """class heirs auto"""

    def __init__(self, brand: str, age: int, mark: str, max_load: int):
        """Adding a required attribute max_load"""
        super().__init__(brand, age, mark)
        self.max_load = max_load
        print(f"max load is {self.max_load}")

    def move(self):
        """Adds to a method 'attention'"""
        print("attention")
        super().move()

    @staticmethod
    def load():
        """When calling the method, we put a pause of 1 second,
        then the load message is issued and again a pause of 1 second"""
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(auto):
    """
    class heir auto
    """

    def __init__(self, brand: str, age: int, mark: str, max_speed: int):
        """adding a required attribute max_speed"""
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


my_auto = auto("bmw", 2003, "e46")
my_auto.move()
my_auto.birthday()
my_auto.stop()

my_auto_1 = Truck("Kamaz", 2017, "te32", 10000)
my_auto_1.move()
my_auto_1.load()

my_auto_2 = Truck("Man", 2020, "e33", 15000)
my_auto_2.move()
my_auto_2.load()

my_auto_3 = Car("Opel", 2021, "astra", 240)
my_auto_3.move()

my_auto_3 = Car("Kia", 2014, "ceed", 220)
my_auto_3.move()
