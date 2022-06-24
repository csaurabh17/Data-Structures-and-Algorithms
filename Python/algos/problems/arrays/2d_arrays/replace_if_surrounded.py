# Given a matrix where every element is either ‘O’ or ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’. A ‘O’ (or a set
# of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above,
# just left and just right of it.

def replace(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            count_true = 0
            # if elem is x continue
            if matrix[i][j] == 'X':
                continue
            # if elem is 0:
            # go down left right up till matrix ends or X is found
            elif matrix[i][j] == 'O':
                # go left
                for k in reversed(range(j)):
                    if matrix[i][k] == 'X':
                        count_true += 1
                        break
                # go right
                for k in range(j, len(matrix[i])):
                    if matrix[i][k] == 'X':
                        count_true += 1
                        break
                # go up
                for k in reversed(range(i)):
                    if matrix[k][j] == 'X':
                        count_true += 1
                        break
                # go down
                for k in range(i + 1, len(matrix)):
                    if matrix[k][j] == 'X':
                        count_true += 1
                        break
                if count_true == 4:
                    matrix[i][j] = 'X'

    return matrix


print(replace([['X', 'O', 'X', 'X', 'X', 'X'],
                     ['X', 'O', 'X', 'X', 'O', 'X'],
                     ['X', 'X', 'X', 'O', 'O', 'X'],
                     ['O', 'X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'O', 'X', 'O'],
                     ['O', 'O', 'X', 'O', 'O', 'O']]))

