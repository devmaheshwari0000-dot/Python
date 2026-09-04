# Example 65: Profiling basics (cProfile)
# Topics: cProfile
import cProfile

def work(n):
    s=0
    for i in range(n): s += i*i
    return s

cProfile.run('work(10000)')

# Task: profile a small function and identify hotspot
