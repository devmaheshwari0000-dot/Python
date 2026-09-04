# Hints:
# - Use strip(), lower(), split() to normalize and split.

# Solution:
s = "  Hello World! This is Python.  "
normalized = s.strip().lower()
words = normalized.split()
print(normalized)
print(words)
