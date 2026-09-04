# Hints:
# - Use __name__ == '__main__' to run script entry point.

# Solution:
def main():
    import sys
    if len(sys.argv) > 1:
        print('Arg:', sys.argv[1])
    else:
        print('No arg')

# Example call commented out
# if __name__ == '__main__':
#     main()
