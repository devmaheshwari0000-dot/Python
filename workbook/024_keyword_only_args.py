# Example 24: Keyword-only arguments
# Topics: enforce keyword-only parameters
def configure(path, *, debug=False, verbose=False):
    print(path, debug, verbose)

configure('/tmp', debug=True)

# Task: create a function with one positional and two keyword-only args
