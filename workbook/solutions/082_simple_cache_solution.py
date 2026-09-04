# Hints:
# - Use collections.deque or OrderedDict to implement LRU; here simple dict+list used for demonstration.

# Solution:
class SimpleLRU:
    def __init__(self, capacity=3):
        self.cap = capacity
        self.data = {}
        self.order = []
    def get(self, k):
        if k in self.data:
            self.order.remove(k)
            self.order.append(k)
            return self.data[k]
        return None
    def put(self, k, v):
        if k in self.data:
            self.order.remove(k)
        elif len(self.order) >= self.cap:
            old = self.order.pop(0)
            del self.data[old]
        self.data[k] = v
        self.order.append(k)

cache = SimpleLRU(2)
cache.put('a',1)
cache.put('b',2)
cache.put('c',3)
print(cache.data)
