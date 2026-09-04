# Hints:
# - Check string reversed equals original for palindrome.

# Solution:
def is_palindrome(s):
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]

print(is_palindrome('Racecar'))
