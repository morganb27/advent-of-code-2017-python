from itertools import count

PUZZLE = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
PART_1 = 0
SEEN = {}

def memory_reallocation(data):
    global PART_1, PART_2, SEEN
    for i in count(start=1):
        m = max(data)
        index = data.index(m)
        data[index] = 0
        PART_1 += 1

        for j in range(1, m + 1):
            data[(index + j )% len(data)] += 1
        
        t = tuple(data)

        if t in SEEN:
            PART_2 = i - SEEN[t]
            break
        else:
            SEEN[t] = i
        

memory_reallocation(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")

