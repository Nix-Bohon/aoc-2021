######################################################
## Part One                                         ##
######################################################
def file_reader():
    with open("day/1/input.txt") as f:
        for line in f:
            yield int(line.strip())


with open("day/1/input.txt") as f:
    previous = None
    increases = 0
    for line in file_reader():
        if previous is not None and line > previous:
            increases += 1
        previous = line

    print("Solution 1:", increases)


######################################################
## Part Two                                         ##
######################################################


def three_item_window(iterator):
    window = []
    for i in iterator:
        window.append(i)
        if len(window) == 4:
            window.pop(0)
        if len(window) == 3:
            yield sum(window)


with open("day/1/input.txt") as f:
    previous = None
    increases = 0
    for line in three_item_window(file_reader()):
        if previous is not None and line > previous:
            increases += 1
        previous = line

    print("Solution 2:", increases)
