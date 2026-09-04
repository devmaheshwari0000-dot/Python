# Hints:
# - Sieve is one approach for prime generator; simple trial division is fine for small n.

# Solution:
def primes_up_to(n):
    def is_prime(k):
        if k < 2: return False
        i = 2
        while i*i <= k:
            if k % i == 0:
                return False
            i += 1
        return True
    for x in range(2, n+1):
        if is_prime(x):
            yield x

print(list(primes_up_to(30)))
