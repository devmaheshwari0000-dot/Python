# Hints:
# - Implement custom encoder by subclassing json.JSONEncoder or by converting to dict.

# Solution:
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

u = User('T', 28)
print(json.dumps(u, cls=UserEncoder))
