# Hints:
# - Use multiprocessing.Pool or Process objects to parallelize work.

# Solution:
from multiprocessing import Pool

def square(x): return x*x

if __name__ == '__main__':
    with Pool(4) as p:
        print(p.map(square, [1,2,3,4]))
