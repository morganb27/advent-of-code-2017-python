import fileinput
from itertools import combinations

PUZZLE = ([int(x) for x in line.strip().split()] for line in fileinput.input())
PART_1, PART_2 = 0, 0

def checksum(data):
    global PART_1, PART_2
    for line in data:

        min_value, max_value = min(line), max(line)
        PART_1 += (max_value - min_value)

        c = [(max(a, b), min(a, b)) for a, b in combinations(line, 2)]
        for (a, b) in c:
            if a % b == 0:
                PART_2 += a // b
                break


print(checksum(PUZZLE))
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")