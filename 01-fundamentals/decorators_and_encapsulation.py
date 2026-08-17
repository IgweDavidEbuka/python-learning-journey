"""
Day 5 — Decorators, encapsulation, @property, operator overloading
"""

def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@shout
def greet():
    return "hello there"

print(greet())  # HELLO THERE


class CardboardCup:
    def __init__(self, size, contents_ounces):
        self.size = size
        self.contents_ounces = contents_ounces

    def __add__(self, other):
        combined_ounces = self.contents_ounces + other.contents_ounces
        return CardboardCup("Combined", combined_ounces)

    def __str__(self):
        return f"{self.size} cup with {self.contents_ounces} oz"


cup_1 = CardboardCup("Medium", 8.0)
cup_2 = CardboardCup("Large", 12.0)
print(cup_1 + cup_2)  # Combined cup with 20.0 oz


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_amount):
        if new_amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_amount


account = BankAccount("Ebuka", 100)
print(account.balance)
account.balance = 500
print(account.balance)
