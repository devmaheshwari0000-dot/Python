# Hints:
# - Counter.most_common helps; split text into words and feed Counter.

# Solution:
from collections import Counter

t = 'this is a test this is'
freq = Counter(t.split())
print(freq)
