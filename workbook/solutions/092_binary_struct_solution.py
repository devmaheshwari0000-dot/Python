# Hints:
# - struct.pack with format 'II' for two unsigned ints.

# Solution:
import struct
b = struct.pack('II', 100, 200)
print(struct.unpack('II', b))
