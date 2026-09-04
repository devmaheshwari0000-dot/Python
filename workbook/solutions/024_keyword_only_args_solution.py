# Hints:
# - Keyword-only args are after * in signature.

# Solution:
def example(pos, *, flag=False, level=1):
    return (pos, flag, level)

print(example(10, flag=True, level=3))
