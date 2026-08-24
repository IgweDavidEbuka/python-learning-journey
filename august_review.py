# LOOPS #

# For loops are used for fixed-size situations
# While loops are used to perform an action based on a certaion condition being true
# The order of operations inside a loop body genuinely matters — printing before updating versus updating before printing produces two completely different sequences, even though both are "valid" loops that run without crashing. This is worth sitting with, since it's an easy thing to get subtly wrong without any error ever appearing.

# While loops
i = 10
while i > 0:
    i -= 3
 
num = 100
while num >= 0:
    print(num)
    num -= 5
        
i = 1

while i < 100:
    print(i)
    i *= 2
    
task = 'quit'
state = False
while state == False:
    test = input("Type 'quit' bro: ")
    if task == test:
        state = True
    else:
        print(test)
        
# For Loops

for i in range(5):
    for j in range(3):
        print(i, j)

for i in range(4,41,4):
    print(i)
    
three = [1 ,2 ,3]
two = [1, 2]

for i in three:
    for j in two:
        print(f"i={i}, j={j}")

def skwir_num(number):
    square = number * number
    return square
      
for num in range(1,7):
    skr = skwir_num(num)
    print(skr)
    
words = ["cat", "elephant", "dog", "hippopotamus"]

for word in words:
    if len(word) > 4:
        print(word)
        
# FUNCTIONS #

# print() always displays something it never hands somn back
# Return is the only way a function can hand a usable value back
# If a function only Print()s and never returns trying to store its walue in a variable will always yields you none
# A parameter is the placeholder name sitting in a functions def
# An arguement is the actual value put in when you call a function

def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)
print(result)

def get_full_name(first, last):
    full_name = first + " " + last
    return(full_name)

name = get_full_name("Ebuka", "Igwe")
print(name.upper())

