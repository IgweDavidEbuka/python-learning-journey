num = int(input("What is your number: "))
value = 100 / num

try:
    print(value)
except ValueError:
    print("This is not number")
except ZeroDivisionError:
    print("Not divisible by 0")
finally:
    print("If this code didn't work check your input.")
    
class NegativeAgeError(ValueError):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age can not be negative")
    return

try:
    set_age(-5)
except ValueError:
    print("Lol wrong value")
except NegativeAgeError as e:
    print(f"Age Invalid: {e}")

