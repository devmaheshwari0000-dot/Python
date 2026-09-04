# Hints:
# - base64.b64encode takes bytes and returns bytes; decode to str.

# Solution:
import base64
import json
obj = {'a':1}
b64 = base64.b64encode(json.dumps(obj).encode()).decode()
print(b64)
print(json.loads(base64.b64decode(b64).decode()))
