# Example 56: JSON + classes (serialization)
# Topics: json, custom encoding
import json
class User:
    def __init__(self, name, age):
        self.name = name; self.age = age

u = User('T', 28)
print(json.dumps({'name': u.name, 'age': u.age}))

# Task: write custom JSON encoder for a class
