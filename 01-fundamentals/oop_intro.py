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


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 60:
            return "Pass"
        else:
            return "Fail"


student_1 = Student("Sonia", 80)
student_2 = Student("Katty", 50)

print(student_1.get_grade())   # Pass
print(student_2.get_grade())   # Fail


# --- Dunder methods: __str__ controls what print() shows ---
class CardboardCup:
    def __init__(self, size, drink, price):
        self.size = size
        self.drink = drink
        self.price = price

    def __str__(self):
        return f"--- Receipt ---\n{self.size} {self.drink}\nTotal: ${self.price:.2f}"


cup = CardboardCup("Large", "Caramel Latte", 4.5)
print(cup)
# --- Receipt ---
# Large Caramel Latte
# Total: $4.50
