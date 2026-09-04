# Hints:
# - Never eval untrusted input; write a simple parser that tokenizes and evaluates safely.

# Solution:
# Very small safe evaluator for + and * using parsing (no eval)

def safe_eval(expr):
    # This is a toy example and does not handle parentheses or errors robustly
    tokens = expr.split()
    # support only sequences like '2 + 3 * 4'
    # first compute all multiplications
    i = 0
    values = []
    ops = []
    while i < len(tokens):
        if tokens[i].isdigit():
            values.append(int(tokens[i]))
        else:
            ops.append(tokens[i])
        i += 1
    # handle * first
    # naive two-pass evaluator
    # convert to new lists
    v2 = [values[0]]
    opidx = 0
    for op in ops:
        if op == '*':
            v2[-1] = v2[-1] * values[opidx+1]
        else:
            v2.append(values[opidx+1])
        opidx += 1
    # then handle +
    return sum(v2)

print(safe_eval('2 + 3 * 4'))
