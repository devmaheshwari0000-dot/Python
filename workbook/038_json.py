# Example 38: JSON handling
# Topics: json.dumps, json.loads
import json
d = {'a':1, 'b':2}
s = json.dumps(d)
print(s)
print(json.loads(s))

# Task: read a JSON file and pretty-print it
