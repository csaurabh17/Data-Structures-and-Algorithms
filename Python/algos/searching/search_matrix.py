# Binary search in a 2d matrix

def search(matrix, target):
    row = 0
    col = len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if target == matrix[row][col]:
            return [row, col]
        elif target > matrix[row][col]:
            row += 1
            # row += 1
        elif target < matrix[row][col]:
            col -= 1

    return [-1, -1]


print(search([[1, 2, 3, 12], [4, 5, 6, 13], [7, 8, 9, 14], [10, 11, 15, 16]], 12))
