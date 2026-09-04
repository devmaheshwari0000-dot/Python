# Hints:
# - Add doctest examples under the function docstring and run doctest.testmod().

# Solution:
def square(x):
    """Return square of x

    >>> square(3)
    9
    >>> square(0)
    0
    """
    return x*x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
