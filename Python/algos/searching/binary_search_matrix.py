# Binary search in a matrix - WIP

def binary_search(matrix, row, column_start, column_end, target):
    while column_start < column_end:
        mid = int(column_start + (column_end - column_start) / 2)
        if target == matrix[row][mid]:
            return [row, mid]
        elif target < matrix[row][mid]:
            column_end -= 1
        elif target > matrix[row][mid]:
            column_start += 1
    return [-1, -1]


def search(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    row_start = 0
    row_end = row - 1
    col_mid = int(col / 2)
    if row == 1:
        return binary_search(matrix, 0, 0, col - 1, target)

    while row_start < row_end - 1:
        mid = int(row_start + (row_end - row_start) / 2)
        if target == matrix[mid][col_mid]:
            return [mid, col_mid]
        elif target < matrix[mid][col_mid]:
            row_end = mid
        else:
            row_start = mid

    if matrix[row_start][mid] == target:
        return [row_start, mid]
    elif matrix[row_end][mid] == target:
        return [row_end, mid]

    if target <= matrix[row_start][col_mid - 1]:
        return binary_search(matrix, row_start, 0, col_mid - 1, target)
    elif target >= matrix[row_start][col_mid + 1]:
        return binary_search(matrix, row_start, col_mid + 1, col - 1, target)
    elif target <= matrix[row_start + 1][col_mid + 1]:
        return binary_search(matrix, row_start + 1, 0, col_mid - 1, target)
    else:
        return binary_search(matrix, row_start + 1, col_mid + 1, col - 1, target)


# WIP
print(search([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6))
