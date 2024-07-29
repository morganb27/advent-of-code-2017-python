import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, 0

def captcha(data):
    global PART_1, PART_2
    half = len(data[0]) // 2
    print(half)
    for line in data:
        for i in range(len(line)):
            if line[i] == line[(i + 1) % len(line)]:
                PART_1 += int(line[i])
            if line[i] == line[(i + half) % len(line)]:
                PART_2 += int(line[i])
            




print(captcha(PUZZLE))
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")