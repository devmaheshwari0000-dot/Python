# Hints:
# - hashlib functions take bytes; read file in binary mode.

# Solution:
import hashlib

def md5_of_bytes(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

print(md5_of_bytes(b'hello'))
