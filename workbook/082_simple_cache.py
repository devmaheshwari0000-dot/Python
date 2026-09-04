# Example 82: Simple caching with dict
# Topics: memoization
cache = {}
def slow(n):
    if n in cache: return cache[n]
    res = sum(range(n))
    cache[n] = res
    return res
print(slow(100))

# Task: implement LRU-like cache with fixed capacity
