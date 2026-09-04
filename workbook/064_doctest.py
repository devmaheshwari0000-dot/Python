# Example 64: doctest example
# Topics: doctest
def square(x):
    """Return square of x

    >>> square(3)
    9
    """
    return x*x

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Task: add doctest examples for another function
