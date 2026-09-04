# Hints:
# - Use time.time() in __enter__/__exit__ or contextmanager that yields.

# Solution:
import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc, tb):
        print('Elapsed:', time.time() - self.start)

with Timer():
    sum(range(100000))
