# Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells
# so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9.


def canPlace(num, matrix, i, j):
    for n in range(9):
        if matrix[i][n] == num:
            return False
        if matrix[n][j] == num:
            return False
        if matrix[3 * int(i/3) + int(i/3)][3 * int(j/3) + int(i%3)] == num:
            return False
    return True


def solve(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for num in range(1, 10):
                    if canPlace(num, matrix, i, j):
                        matrix[i][j] = num
                        if solve(matrix):
                            return True
                        else:
                            matrix[i][j] = 0
                return False
    print(matrix)
    return True


solve([ [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ])