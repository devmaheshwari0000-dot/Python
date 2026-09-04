# Example 20: zip() and enumerate()
# Topics: combine iterables, get index
names = ['a', 'b', 'c']
scores = [10,20,30]
for i, (n, s) in enumerate(zip(names, scores)):
    print(i, n, s)

# Task: merge two lists into a dict using zip
