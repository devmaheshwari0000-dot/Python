# Hints:
# - Use built-in max on args.

# Solution:
def max_of_args(*args):
    if not args:
        return None
    return max(args)

print(max_of_args(3,5,2))
