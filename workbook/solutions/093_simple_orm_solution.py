# Hints:
# - to_dict can return self.__dict__; from_dict can construct via **kwargs.

# Solution:
class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def to_dict(self):
        return dict(self.__dict__)
    @classmethod
    def from_dict(cls, d):
        return cls(**d)

r = Record(id=1, name='Alice')
print(r.to_dict())
print(Record.from_dict({'id':2,'name':'Bob'}).name)
