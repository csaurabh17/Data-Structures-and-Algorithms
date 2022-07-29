# solving node queens problem in a given X BY X matrix

def is_safe(board, row, col):
    # for upper
    for i in range(row):
        if board[i][col]:
            return False

    # for left diagonal
    max_left = min(row, col)
    for i in range(max_left + 1):
        if board[row - i][col - i]:
            return False

    # for right diagonal
    max_right = min(row, len(board) - 1 - col)
    for i in range(max_right + 1):
        if board[row - i][col + i]:
            return False

    return True


def display(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                print("Q ", end="")
            else:
                print("x ", end="")
        print("")


def n_queens(board, row):
    # print(row, '------', len(board))
    if row == len(board):
        display(board)
        print("-------")
        return 1

    count = 0

    for col in range(len(board)):
        # print(is_safe(board, row, col))
        if is_safe(board, row, col):
            # print(row, col)
            board[row][col] = True
            count += n_queens(board, row + 1)
            board[row][col] = None
    return count


n = 4
print(n_queens([[None] * n for i in range(n)], 0))
