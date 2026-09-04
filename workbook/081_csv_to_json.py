# Example 81: CSV to JSON small utility
# Topics: csv, json
import csv, json
# Read CSV and convert to JSON list (example with a hardcoded list)
rows = [['name','age'], ['Ann','30']]
keys = rows[0]
json_list = [dict(zip(keys, r)) for r in rows[1:]]
print(json.dumps(json_list))

# Task: implement function csv_to_json(path_in, path_out)
