# Hints:
# - Base cases for recursion: n <= 1.

# Solution:
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

print([fib_rec(i) for i in range(10)])
