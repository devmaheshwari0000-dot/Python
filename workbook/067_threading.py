# Example 67: Threading basics
# Topics: threading.Thread
from threading import Thread

def worker(n):
    print('thread', n)

# t = Thread(target=worker, args=(2,)); t.start(); t.join()

# Task: start 5 threads that increment a shared counter with proper locking
