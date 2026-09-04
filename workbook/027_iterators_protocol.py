# Example 27: Iterators protocol
# Topics: __iter__, __next__
class Counter:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return self.i

for x in Counter(3):
    print(x)

# Task: implement an iterator that iterates over Fibonacci numbers
