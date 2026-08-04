"""
Day 2 — Functions: def, parameters, positional/keyword args, return vs print
"""

# --- def vs calling, and what a bare reference (no parens) is ---
def greet():
    print("Hello!")

greet()          # actually runs it
# greet          # a reference to the function itself, not executed


# --- Single parameter ---
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Ebuka")
greet_name("Tonye")


# --- Multiple parameters, positional ---
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Ebuka", 25)


# --- Positional vs keyword arguments ---
def calculate_total(item, price, quantity):
    total = price * quantity
    print(f"{quantity}x {item} = ${total}")

calculate_total("Coffee", 5, 3)                          # positional
calculate_total(quantity=3, item="Coffee", price=5)       # keyword, different order


# --- return vs print ---
def add_return(a, b):
    return a + b

result = add_return(3, 4)
print(result)  # 7 — return hands back a usable value


def square(n):
    return n ** 2

print(square(5))  # 25 — return's value plugged straight into print()


# --- Final exercise: combining params + return + using the result ---
def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

final_price = calculate_discount(200, 25)
print(f"Final price after discount: ${final_price}")  # $150.0
