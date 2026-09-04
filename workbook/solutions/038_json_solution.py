# Hints:
# - json.load/json.dump for files; json.loads/dumps for strings.

# Solution:
import json

d = {'a':1, 'b':2}
with open('/tmp/example_json.json', 'w') as f:
    json.dump(d, f)
with open('/tmp/example_json.json') as f:
    data = json.load(f)
print(data)
