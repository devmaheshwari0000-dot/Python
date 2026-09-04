# Hints:
# - WeakValueDictionary holds weak refs to values so they can be GC'd.

# Solution:
import weakref
class A: pass
cache = weakref.WeakValueDictionary()
a = A()
cache['a'] = a
print('cached:', cache.get('a'))
del a
import gc; gc.collect()
print('after del:', cache.get('a'))
