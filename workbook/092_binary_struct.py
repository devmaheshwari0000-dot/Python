# Example 92: Handling binary data
# Topics: bytes, struct
import struct
b = struct.pack('I', 1024)
print(b, struct.unpack('I', b))

# Task: pack two ints and unpack them
