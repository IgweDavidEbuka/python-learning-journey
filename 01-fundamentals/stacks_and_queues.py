"""
Stacks and Queues — LIFO vs FIFO, plus why deque beats a list for queues at scale
"""

# --- STACK (LIFO — Last In, First Out) ---
class Shoe:
    def __init__(self, owner):
        self.owner = owner

class ShoeRack:
    def __init__(self):
        self._shoes = []

    def push(self, shoe):
        self._shoes.append(shoe)  # add to the top

    def is_empty(self):
        return len(self._shoes) == 0

    def pop(self):
        if self.is_empty():
            print("Action Blocked: Rack is empty")
            return None
        return self._shoes.pop()  # remove from the top — last one in comes out first

    def show_all(self):
        return self._shoes


rack = ShoeRack()
shoe1 = Shoe("Ebuka")
shoe2 = Shoe("Eileen")
rack.push(shoe1)
rack.push(shoe2)

popped = rack.pop()
print(popped.owner)  # Eileen — last pushed, first popped (LIFO)


# --- QUEUE (FIFO — First In, First Out) ---
class BookQueue:
    def __init__(self):
        self._books = []

    def enqueue(self, book):
        self._books.append(book)  # add to the back

    def is_empty(self):
        return len(self._books) == 0

    def dequeue(self):
        if self.is_empty():
            print("Action Blocked: Queue empty")
            return None
        return self._books.pop(0)  # remove from the front — O(n), shifts every remaining item

    def show_all(self):
        return self._books


library = BookQueue()
library.enqueue("Seven Deadly Sins")
library.enqueue("Tales of Dragons")

first_out = library.dequeue()
print(first_out)  # Seven Deadly Sins — first in, first out (FIFO)


# --- Why .pop(0) is slow at scale ---
# A list is one contiguous block of memory. Removing index 0 forces every
# remaining item to shift down one position to close the gap — O(n) cost,
# growing with list size. .append() / .pop() (no arg) work on the END,
# so nothing shifts — O(1), fast regardless of size.


# --- deque: the fix for large/high-throughput queues ---
from collections import deque

class BookQueueFast:
    def __init__(self):
        self._books = deque()

    def enqueue(self, book):
        self._books.append(book)

    def is_empty(self):
        return len(self._books) == 0

    def dequeue(self):
        if self.is_empty():
            print("Action Blocked: Queue empty")
            return None
        return self._books.popleft()  # amortized O(1) — no shifting, unlike list.pop(0)


fast_library = BookQueueFast()
fast_library.enqueue("Seven Deadly Sins")
fast_library.enqueue("Tales of Dragons")
print(fast_library.dequeue())  # Seven Deadly Sins
