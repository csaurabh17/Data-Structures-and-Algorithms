# https://leetcode.com/problems/set-matrix-zeroes/

def set_zeroes(matrix):
    is_zero = True
    cols = len(matrix[0])

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            is_zero = False
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0

    for i in reversed(range(len(matrix))):
        for j in reversed(range(cols)):
            if i == 0 and j == cols - 1:
                if matrix[0][0] == 0 and is_zero:
                    matrix[i][j] = 0
                elif not is_zero:
                    continue
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    print(matrix)


set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
