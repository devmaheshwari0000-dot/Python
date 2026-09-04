# Hints:
# - Use a dict and increment counts for each char.

# Solution:
s = "banana"
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
