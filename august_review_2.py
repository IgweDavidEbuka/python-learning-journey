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