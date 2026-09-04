# Example 66: Multiprocessing basics
# Topics: multiprocessing.Process
from multiprocessing import Process

def worker(n):
    print('worker', n)

p = Process(target=worker, args=(1,))
# p.start(); p.join()  # commented to avoid spawning processes in restricted env

# Task: sum numbers in parallel using multiple processes
