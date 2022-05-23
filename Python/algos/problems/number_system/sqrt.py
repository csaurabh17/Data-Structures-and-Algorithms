def sqrt(n):
    start = 0
    end = n
    while start <= end:
        mid = (start + (end - start) / 2)
        if mid * mid < n:
            start = mid + 1
        elif mid * mid > n:
            end = mid - 1
        else:
            return mid

    root = 0.0
    incr = 0.1
    for i in range(1, 4):
        while root * root <= n:
            root += incr
    root -= incr
    incr /= 10

    return root


print(sqrt(40))
