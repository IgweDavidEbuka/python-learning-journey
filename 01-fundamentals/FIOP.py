# Creating, Reading and Writing a file

with open("journal.txt", "w") as file:
    file.write("Day 1: Started learning file I/O")
    
with open("journal.txt", "a") as file:
    file.write("\nDay 2: Practicing reading and writing")
    
with open("journal.txt", "r") as file:
    print(file.read())