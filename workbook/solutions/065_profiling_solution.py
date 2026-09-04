# Hints:
# - Use cProfile.run or Profile object to collect timings and examine stats.

# Solution:
import cProfile

def work(n):
    s=0
    for i in range(n): s += i*i
    return s

cProfile.run('work(10000)')
