# Hints:
# - Use memoryview to change bytes without copying.

# Solution:
b = bytearray(b'hello')
v = memoryview(b)
v[0] = ord('H')
print(b)
