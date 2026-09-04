# Example 37: Regular expressions
# Topics: re module, search, match, findall
import re
text = 'My email is test@example.com'
print(re.findall(r'[\w.-]+@[\w.-]+', text))

# Task: extract all URLs from a text using regex
