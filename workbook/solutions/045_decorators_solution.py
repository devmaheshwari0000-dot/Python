# Hints:
# - Decorator wraps function and returns wrapper; use time.time() to measure.

# Solution:
from functools import wraps
import time

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.6f}s")
        return res
    return wrapper

@timed
def work(n):
    s = 0
    for i in range(n): s += i
    return s

work(100000)
