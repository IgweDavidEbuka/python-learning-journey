# Self refers to the whichever specific object called the method and anywhere self.somn appeared in that method. Reading and writing particular object attributes.
# Self is re-bound to a different object each time a method is called.
# When a child class defines its own __init__ completely overrides of its parent. 
# Overrides erase parents innit.
# super().__init__() allows us to use the original setup of the parents in a child using thier own attributes. The attributes are put into the init backets
# Inheriting from a class does not mean every method automatically runs.
# Super(), lets a child's overriding method call the parent's original version of that same method, so you get both the parent's original behavior and whatever new behavior the child adds — instead of the child's version completely replacing the parent's.



class Animal:
    def __init__(self):
        self.type = "animal"
        self.sound = "nothing"
    
    def make_sound(self):
        return f"the {self.type} goes {self.sound}"
    
class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.type = "bird"
    
    def make_sound(self):
        return super().make_sound() + "tweet"
    
bird = Bird()
print(bird.make_sound())

class SpaceMarine:
    def __init__(self, Aliance):
        self.Aliance = Aliance
    
    def __str__(self):
        return f"Name: {self.name} | Alliegence: {self.Aliance}"
    
class AThousandSons(SpaceMarine):
    def __init__(self, Aliance, name):
        super().__init__(Aliance)
        self.name = name
    

Marine1 = AThousandSons("Chaos", "Batiatus")
print(Marine1)


def silence(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper

def vocalise():
    return "Hi The Sumbish"

silunce = silence(vocalise)
print(silunce)

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_amount):
        if new_amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_amount
        
# For manual property or buff allocation. The function followed by another function in it that will be used to apply said change within it.
# @ makes is so there doesn't have to be a reassignment line. Just call @function before using a function.
# A setter method is called upon when a direct method(@property) is called on an attribute of an innit method. With a .setter which is used to set cases such as the one above.