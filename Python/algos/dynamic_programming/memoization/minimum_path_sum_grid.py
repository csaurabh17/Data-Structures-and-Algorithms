# Microsoft - Minimum path sum in grid
import sys


def min_path_sum(current_index, grid):
    end_index = [len(grid) - 1, len(grid[0]) - 1]
    if current_index == end_index:
        return grid[len(grid) - 1][len(grid[0]) - 1]

    min_value = sys.maxsize
    i, j = current_index
    if i < end_index[0]:
        min_value = min(min_value, grid[i][j] + min_path_sum([i + 1, j], grid))
    if j < end_index[1]:
        min_value = min(min_value, grid[i][j] + min_path_sum([i, j + 1], grid))

    return min_value


print(min_path_sum([0, 0], [[5, 9, 6], [11, 5, 2]]))
