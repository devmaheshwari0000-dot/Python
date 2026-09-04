# Example 72: Weak references
# Topics: weakref
import weakref
class A: pass
a = A()
r = weakref.ref(a)
print(r())
del a
print(r())

# Task: use WeakValueDictionary to cache objects without preventing GC
