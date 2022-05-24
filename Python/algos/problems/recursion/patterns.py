# printing patterns using recursion

# * * * *
# * * *
# * *
# *

def pattern_1(rows, cols):
    if rows == 0:
        return
    if rows > cols:
        print("*", end=" ")
        pattern_1(rows, cols + 1)
    else:
        print("")
        pattern_1(rows - 1, 0)


# *
# * *
# * * *
# * * * *

def pattern_2(rows, cols):
    if rows == 0:
        return
    if rows > cols:
        pattern_2(rows, cols + 1)
        print("*", end=" ")
    else:
        pattern_2(rows - 1, 0)
        print("")


pattern_1(4, 0)
pattern_2(4, 0)
