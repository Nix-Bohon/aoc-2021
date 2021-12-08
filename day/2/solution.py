######################################################
## Part One                                         ##
######################################################
def file_reader():
    with open("day/2/input.txt") as f:
        for line in f:
            direction, unit = line.split(" ")
            unit = int(unit)
            yield direction, unit


depth = distance = 0
for d, u in file_reader():
    if d == "forward":
        distance += u
    elif d == "down":
        depth += u
    elif d == "up":
        depth -= u

print("solution 1:")
print(f"depth={depth}, distance={distance}")
print(f"distance * depth =", depth * distance)


######################################################
## Part Two                                         ##
######################################################

depth = distance = aim = 0
for d, u in file_reader():
    if d == "forward":
        distance += u
        depth += u * aim
    elif d == "down":
        aim += u
    elif d == "up":
        aim -= u

print("solution 2:")
print(f"depth={depth}, distance={distance}")
print(f"distance * depth =", depth * distance)
