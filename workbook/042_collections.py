# Example 42: Collections (defaultdict, Counter)
# Topics: collections
from collections import defaultdict, Counter
d = defaultdict(int)
d['a'] += 1
print(d)
print(Counter(['a','b','a']))

# Task: count word frequencies in a paragraph using Counter
