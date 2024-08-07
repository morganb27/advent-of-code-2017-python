import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
BOTTOM = ''

D = defaultdict(dict)

def recursive_circus(data):
    global BOTTOM
    for line in data:
        name, weight, children = parse_input(line)
        D[name]['weight'] = weight
        D[name]['children'] = children
    add_parents(D)
    for key, value in D.items():
        if 'parent' not in value:
            BOTTOM = key

def add_parents(graph):
    for parent, values in graph.items():
        for x in values['children']:
            D[x]['parent'] = parent

def parse_input(line):
    children = []
    if " -> " in line:
        left, right = line.split(" -> ")
        name, weight = left.strip(")").split(" (")
        children = right.split(", ")
    else:
        name, weight = line.strip(")").split(" (")
    return name, weight, children

recursive_circus(PUZZLE)
print(f"Solution to part 1 is: {BOTTOM}")