# Given a 2D matrix, print all elements of the given matrix in diagonal order. For example, consider the following 5
# X 4 input matrix

def print_diagonally(arr):
    i = 0
    j = 0
    c = len(arr) - 1

    # i loop
    while i <= c:
        inner_i = i
        while j <= i:
            print(arr[inner_i][j], end=" ")
            j += 1
            inner_i -= 1
        print()
        j = 0
        i += 1

    j = i - (len(arr) - 1)
    i = i - 1
    c += 1
    while j <= len(arr[len(arr) - 1]) and i < len(arr):
        inner_i = i
        while inner_i >= 0 and j < len(arr[inner_i]):
            print(arr[inner_i][j], end=" ")
            if inner_i == len(arr) - 1 and j == len(arr[inner_i]) - 1:
                break
            j += 1
            inner_i -= 1
        print()
        c += 1
        j = c - i


print_diagonally([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

print_diagonally([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
