# Example 78: Base64 encoding
# Topics: base64
import base64
s = base64.b64encode(b'hello').decode()
print(s)
print(base64.b64decode(s))

# Task: encode a JSON object as base64 and decode it back
