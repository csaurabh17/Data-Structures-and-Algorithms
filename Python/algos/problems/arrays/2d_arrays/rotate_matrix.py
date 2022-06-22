# https://leetcode.com/problems/rotate-image/

def rotate_matrix(matrix):
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r):
            top, bottom = l, r

            # assigning top let value to temp variable
            temp = matrix[top][l + i]

            # moving bottom left to top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # moving bottom right to bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # moving top right to bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # putting temp value in bottom right
            matrix[top + i][r] = temp

        l += 1
        r -= 1
    print(matrix)


rotate_matrix([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
