import fileinput
from collections import defaultdict
from pprint import pprint

PUZZLE = [line.strip() for line in fileinput.input()]
BOTTOM = ''

D = defaultdict(dict)
C = defaultdict(dict)

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
    root = BOTTOM
    unbalanced_node(root, D)



def unbalanced_node(node, tree):
    total_weight = int(D[node]['weight'])
    C = defaultdict(dict)

    for child in D[node]['children']:
        child_weight = unbalanced_node(child, tree)
        C[node][child] = child_weight
        total_weight += int(child_weight)

    for key, weights in C.items():
        unique_weights = set(weights.values())
        if len(unique_weights) > 1:
            print(key, weights)
            for item in weights:
                print(item, D[item]['weight'])
    return total_weight

        


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