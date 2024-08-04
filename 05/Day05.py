import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]

def maze_part_one(data):
    steps = 0
    instructions = [int(x) for x in data]
    i = 0
    while i >= 0 and i < len(instructions):
        curr = instructions[i]
        instructions[i] += 1
        i += curr
        steps += 1
    return steps

def maze_part_two(data):
    steps = 0
    instructions = [int(x) for x in data]
    i = 0
    while i >= 0 and i < len(instructions):
        curr = instructions[i]
        instructions[i] += (-1 if curr >= 3 else 1)
        i += curr
        steps += 1
    return steps

print(f"Solution to part 1 is: {maze_part_one(PUZZLE)}")
print(f"Solution to part 2 is: {maze_part_two(PUZZLE)}")
