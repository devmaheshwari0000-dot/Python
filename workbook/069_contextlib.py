# Example 69: Contextlib utilities
# Topics: contextlib.contextmanager
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    start = time.time()
    try:
        yield
    finally:
        print(name, 'took', time.time() - start)

with timer('work'):
    sum(range(10000))

# Task: create a contextmanager that logs exceptions
