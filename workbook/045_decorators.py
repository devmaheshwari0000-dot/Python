# Example 45: Decorators basics
# Topics: function decorators
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a,b): return a+b
print(add(2,3))

# Task: write a decorator that times a function
