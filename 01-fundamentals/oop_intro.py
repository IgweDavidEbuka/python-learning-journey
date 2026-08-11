"""
Day 4 — OOP fundamentals: class, __init__, self, methods, object independence
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


my_rect = Rectangle(5, 3)
print(my_rect.area())        # 15
print(my_rect.perimeter())   # 16
