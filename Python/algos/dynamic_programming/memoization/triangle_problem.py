# to solve triangle problem with fixed start point and variable end point
import sys


def min_path(up, total, n, idx):
    i, j = idx
    if i == len(up) - 1:
        return total
    if [i, j] == [0, 0]:
        total = up[i][j]
    min_value = min(min_path(up, total + up[i + 1][j], i + 1, [i + 1, j]),
                    min_path(up, total + up[i + 1][j + 1], i + 1, [i + 1, j + 1]))

    return min_value


print(min_path([[1], [2, 3], [3, 6, 7], [9, 8, 6, 1]], 0, 4, [0, 0]))
