# Hints:
# - Use threading.Lock to protect shared state.

# Solution:
from threading import Thread, Lock

counter = 0
lock = Lock()

def worker(n):
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

threads = [Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print('Counter:', counter)
