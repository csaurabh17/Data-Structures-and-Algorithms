# https://leetcode.com/problems/spiral-matrix/

def spiral_traversal(matrix):
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1
    i = 0
    j = 0

    while left != right:
        # going right
        while j <= right:
            print(matrix[i][j], end=" ")
            j += 1
        print()
        j = right
        top += 1
        i += 1

        # going down
        while i <= bottom:
            print(matrix[i][j], end=" ")
            i += 1
        print()
        i = bottom
        right -= 1
        j -= 1

        if not (left < right or top < bottom):
            break

        # going left
        while j >= left:
            print(matrix[i][j], end=" ")
            j -= 1
        print()
        bottom -= 1
        i -= 1
        j = left
        # going up
        while i >= top:
            print(matrix[i][j], end=" ")
            i -= 1
        print()
        left += 1
        i += 1
        j += 1


spiral_traversal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
