# Hints:
# - Slicing with [start:stop:step].

# Solution:
def every_third_from_index1(lst):
    return lst[1::3]

print(every_third_from_index1(list(range(10))))
