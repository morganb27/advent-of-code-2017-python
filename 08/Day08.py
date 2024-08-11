import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
D = defaultdict(int)
HIGHEST_VALUE = 0
HIGHEST_VALUE_HELD = float('-inf')

eq_functions = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '==': lambda x, y: x == y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '!=': lambda x, y: x != y
}

def registers(data):
    global HIGHEST_VALUE, HIGHEST_VALUE_HELD
    for line in data:
        x, op, i, y, eq, j = parse_input(line)
        print(eq)
        if x not in D:
            D[x] = 0
        if y not in D:
            D[y] = 0
        if eq_functions[eq](D[y], j):
            D[x] += i * (1 if op == 'inc' else -1)
            HIGHEST_VALUE_HELD = max(HIGHEST_VALUE_HELD, D[x])

    HIGHEST_VALUE = max(D.values())

def parse_input(line):
    left, right = line.split(' if ')
    x, op, i = left.split()
    y, eq, j = right.split()
    return x, op, int(i), y, eq, int(j)

registers(PUZZLE)
print(f"Solution to part 1 is: {HIGHEST_VALUE}")
print(f"Solution to part 2 is: {HIGHEST_VALUE_HELD}")