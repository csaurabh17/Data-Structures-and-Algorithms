# printing patterns using recursion

# * * * *
# * * *
# * *
# *

def pattern_1(rows, cols):
    if rows <= 0:
        return
    if rows == cols:
        print("*", end=" ")
        return
    elif rows - cols >= 2:
        print("*", end=" ")
        pattern_1(rows, cols + 1)
    elif rows - cols == 1:
        print("* ")
        pattern_1(rows - 1, 0)


pattern_1(4, 0)
