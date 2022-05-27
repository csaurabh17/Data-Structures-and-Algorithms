# number of ways to reach the last block of matrix


def count_ways(current_index, end_index):
    if current_index == end_index:
        return 1
    count = 0

    i, j = current_index

    if i < end_index[0]:
        count += count_ways([i + 1, j], [2, 2])
    if j < end_index[1]:
        count += count_ways([i, j + 1], [2, 2])
    return count


def print_ways(path, current_index, end_index):
    if current_index == end_index:
        print(path)

    i, j = current_index

    if i < end_index[0]:
        print_ways(path + "R", [i + 1, j], [2, 2])
    if j < end_index[1]:
        print_ways(path + "D", [i, j + 1], [2, 2])

    return path


print(count_ways([0, 0], [2, 2]))
print(print_ways("", [0, 0], [2, 2]))
