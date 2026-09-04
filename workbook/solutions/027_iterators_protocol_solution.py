# Hints:
# - Implement __iter__ to return self and __next__ to advance.

# Solution:
class FibIter:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.i += 1
        return val

print(list(FibIter(6)))
