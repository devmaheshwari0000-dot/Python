# Hints:
# - Read CSV header row, then map subsequent rows into dicts with zip.

# Solution:
import csv, json
rows = [['name','age'], ['Ann','30']]
keys = rows[0]
json_list = [dict(zip(keys, r)) for r in rows[1:]]
print(json.dumps(json_list))
