# Hints:
# - Use lru_cache decorator to memoize recursive functions.

# Solution:
from functools import lru_cache

@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
