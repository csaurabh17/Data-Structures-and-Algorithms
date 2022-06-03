def stair_climb(p, up, n):
    if n == 0:
        return 1
    if not up:
        return 0
    if n < 0:
        return 0

    count = 0
    for i in range(len(up)):
        count += stair_climb(p + up[i], up, n - up[i])

    return count


print(stair_climb(0, [1, 2], 3))
