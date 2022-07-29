# Solving 0-1 Knapsack
# [1, 3, 4, 5] - [1, 4, 5, 7] - Knapsack weight is 7

# with memoization - assuming node constraint is 100 and size is 1000
t = [[-1] * 200 for i in range(200)]


def find_max_profit(weight_arr, value_arr, size):
    if len(weight_arr) == 0 or size == 0:
        return 0

    if t[size][len(weight_arr)] != -1:
        return t[size][len(weight_arr)]

    if weight_arr[len(weight_arr) - 1] <= size:
        t[size][len(weight_arr)] = max(
            weight_arr[len(weight_arr) - 1] + find_max_profit(weight_arr[:-1], value_arr[:-1],
                                                              size - weight_arr[len(weight_arr) - 1]),
            find_max_profit(weight_arr[:-1], value_arr[:-1], size))
        return t[size][len(weight_arr)]
    else:
        return find_max_profit(weight_arr[:-1], value_arr[:-1], size)


print(find_max_profit([1, 4, 5, 7], [1, 3, 4, 5], 14))
print(find_max_profit([10, 20, 30], [60, 100, 120], 50))

