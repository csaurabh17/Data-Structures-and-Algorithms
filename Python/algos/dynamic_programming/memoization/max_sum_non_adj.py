def max_sum(p, arr):
    if not arr:
        return p

    max_value = 0
    for i in range(len(arr)):
        max_value = max(max_value, max_sum(p + arr[i], arr[i + 2:]))

    return max_value


print(max_sum(0, [1, 4, 7, 10, 11]))
