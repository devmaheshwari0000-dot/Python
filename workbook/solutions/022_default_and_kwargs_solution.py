# Hints:
# - kwargs is a dict: sorted(kwargs.keys()).

# Solution:
def print_sorted_keys(**kwargs):
    for k in sorted(kwargs.keys()):
        print(k)

print_sorted_keys(b=2, a=1, c=3)
