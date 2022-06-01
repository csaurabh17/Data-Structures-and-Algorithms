# Solving 0-1 Knapsack
# [1, 3, 4, 5] - [1, 4, 5, 7] - Knapsack weight is 7

def find_max_profit(weight_arr, value_arr, size):
    if len(weight_arr) == 0 or size == 0:
        return 0

    if weight_arr[len(weight_arr) - 1] <= size:
        return max(weight_arr[len(weight_arr) - 1] + find_max_profit(weight_arr[:-1], value_arr[:-1], size - weight_arr[len(weight_arr) - 1]),
                   find_max_profit(weight_arr[:-1], value_arr[:-1], size))
    else:
        return find_max_profit(weight_arr[:-1], value_arr[:-1], size)


print(find_max_profit([1, 4, 5, 7], [1, 3, 4, 5], 7))
