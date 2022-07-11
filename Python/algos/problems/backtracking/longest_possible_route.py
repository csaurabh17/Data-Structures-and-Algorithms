# Given an M x N matrix, with a few hurdles arbitrarily placed, calculate the length of the longest possible route
# possible from source to a destination within the matrix. We are allowed to move to only adjacent cells which are
# not hurdles. The route cannot contain any diagonal moves and a location once visited in a particular path cannot be
# visited again.

def solve2(matrix, destination, current, total):
    i, j = current
    if i >= len(matrix) or j >= len(matrix[i]):
        return 0
    if i < 0 or j < 0:
        return 0
    if matrix[i][j] == 0 or matrix[i][j] == 'X':
        return 0
    if current == destination:
        return total

    matrix[i][j] = 'X'
    val = 0
    val = max(val, solve2(matrix, destination, [i, j + 1], total + 1))
    val = max(val, solve2(matrix, destination, [i + 1, j], total + 1))
    val = max(val, solve2(matrix, destination, [i, j - 1], total + 1))
    val = max(val,solve2(matrix, destination, [i - 1, j], total + 1))
    matrix[i][j] = 1
    return val


print(solve2([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [1, 7], [0, 0], 0))

print(solve2([[1, 1, 0, 1, 0, 1],
             [0, 1, 1, 1, 0, 1],
             [1, 1, 1, 1, 1, 1],
             [0, 0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1, 1]], [3, 3], [2, 2], 0))
