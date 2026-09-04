# Hints:
# - Use random.randint and random.choice in loops to estimate probability.

# Solution:
import random

def estimate_prob(num_trials=1000):
    count = 0
    for _ in range(num_trials):
        s = random.randint(1,6) + random.randint(1,6)
        if s == 7:
            count += 1
    return count / num_trials

print(estimate_prob(1000))
