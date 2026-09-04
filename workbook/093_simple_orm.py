# Example 93: Simple ORM-like mapping (example)
# Topics: simple class mapping to dict
class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

r = Record(id=1, name='Alice')
print(r.name)

# Task: implement to_dict() and from_dict() methods
