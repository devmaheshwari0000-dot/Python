# Example 44: Functional programming utilities
# Topics: functools, lru_cache
from functools import lru_cache
@lru_cache()
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
print(fib(20))

# Task: apply lru_cache to memoize a slow function and measure speedup
