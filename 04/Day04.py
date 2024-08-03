import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, 0

def passphrase(data):
    global PART_1, PART_2
    for line in data:
        PART_1 += is_valid_passphrase(line.split())
        PART_2 += is_valid_passphrase_part_two(line.split())

def is_valid_passphrase(arr):
    return len(arr) == len(set(arr))

def is_valid_passphrase_part_two(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if are_anagrams(arr[i], arr[j]):
                return False
    return True

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)



passphrase(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")