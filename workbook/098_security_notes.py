# Example 98: Security basics (input validation)
# Topics: sanitize inputs, avoid eval
unsafe = "__import__('os').system('echo hacked')"
# Never eval untrusted input
print('Do not run eval on untrusted strings')

# Task: write a safe parser for simple arithmetic expressions (support + and *)
