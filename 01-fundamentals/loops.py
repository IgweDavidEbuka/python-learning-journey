"""
Day 1 — Loops (for/while), nesting, comprehensions, map/filter/sorted
"""

# --- Manual counter tracing (while loop) ---
i = 0
while i < 10:
    print(i)
    i += 2
# Output: 0, 2, 4, 6, 8


# --- Nested loops: multiplication table (1-3) ---
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} X {j} = {i * j}")


# --- Building a list manually with a loop ---
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]


# --- Same result, as a list comprehension ---
squares_comp = [n ** 2 for n in range(1, 6)]
print(squares_comp)  # [1, 4, 9, 16, 25]

cubes = [n ** 3 for n in range(1, 5)]
print(cubes)  # [1, 8, 27, 64]


# --- map(): apply a function to every item ---
letters = ["a", "b", "c"]
upper_letters = list(map(str.upper, letters))
print(upper_letters)  # ['A', 'B', 'C']


# --- filter(): keep only items matching a condition ---
animals = ["cat", "elephant", "dog", "giraffe"]
long_animals = list(filter(lambda x: len(x) > 3, animals))
print(long_animals)  # ['elephant', 'giraffe']


# --- sorted(): reorder using a key, optionally reversed ---
sorted_animals = sorted(animals, key=len, reverse=True)
print(sorted_animals)  # ['elephant', 'giraffe', 'cat', 'dog']
