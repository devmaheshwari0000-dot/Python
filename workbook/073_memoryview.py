# Example 73: Memoryview and bytearray
# Topics: memoryview, bytearray
b = bytearray(b'hello')
v = memoryview(b)
v[0] = ord('H')
print(b)

# Task: modify a slice of a bytearray using memoryview
