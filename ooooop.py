
def shout(func):
    def wrapper():
        result = func()
        return result.upper
    return wrapper

@shout
def greet():
    return "hello there"

print(greet())