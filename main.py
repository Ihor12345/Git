import random
from time import sleep

class Human:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.plane = None
        self.gladness = 50
        self.money = 20
    def greeting(self, human):
        print(f"Hello {human.name}, I am {self.name}")
    def drive(self):
        if self.car:
            self.car.drive()

    def fly(self):
        if self.plane:
            self.plane.fly()

    def work(self):
        self.money += random.randint(5, 10)
        self.gladness -= random.randint(2, 5)
    def rest(self):
        self.money -= random.randint(1, 10)
        self.gladness += random.randint(2, 5)

class Car:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        self.owner = None
    def drive(self):
        print(f"{self.name} chux-chux")
    def buy(self, human):
        if not self.owner:
            if human.money >= self.price:
                human.car = self
                self.owner = human
                print(f"{human.name} купил {self.name}")
            else:
                print(f"{human.name} недостаточно средств купить {self.name}")
        else:
            print(f"{self.name} уже приобретена {self.owner.name}")

class Plane:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        self.owner = None
    def fly(self):
        print(f"{self.name} uuuu-uuuu")
    def buy(self, human):
        if not self.owner:
            if human.money >= self.price:
                human.plane = self
                self.owner = human
                print(f"{human.name} купил {self.name}")
            else:
                print(f"{human.name} недостаточно средств купить {self.name}")
        else:
            print(f"{self.name} уже приобретена {self.owner.name}")

class Home:
    def __init__(self):
        self.humans = []
    def add(self, human):
        self.humans.append(human)
    def greetingAll(self):
        for human in self.humans:
            for some_human in self.humans:
                if human != some_human:
                    human.greeting(some_human)

h1 = Human("Kolya")
h2 = Human("Olya")
h3 = Human("Vadim")
h4 = Human("Nastya")
h5 = Human("Kristina")
h6 = Human("Sergey")
h7 = Human("Andrey")
h8 = Human("Polina")

home = Home()

home.add(h1)
home.add(h2)
home.add(h3)
home.add(h4)
home.add(h5)
home.add(h6)
home.add(h7)
home.add(h8)

autopark = [
    Car("BMW", 2019, 200),
    Car("Bentli", 2017, 300),
    Car("Bugatti", 2016, 100),
    Car("Toyota", 2022, 600),
]
angar = [
    Plane("Ан-2", 2015, 900),
    Plane("U-2", 2013, 905),
    Plane("Як-42", 2016, 599),
    Plane("DC-10", 2019, 800),
]

day = 1
while True:
    print("Day: ", day)
    for human in home.humans:
        actions = [human.work, human.rest]
        random.choice(actions)()
        if random.randint(1, 100) <= 5:
            sleep(2)
            random.choice(autopark).buy(human)
    day += 1


