# Example 19: map(), filter(), reduce()
# Topics: functional tools
nums = [1, 2, 3, 4]
sq = list(map(lambda x: x*x, nums))
ev = list(filter(lambda x: x%2==0, nums))
print(sq, ev)

# Task: use reduce to compute product of list elements
