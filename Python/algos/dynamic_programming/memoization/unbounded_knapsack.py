# solving unbounded knapsack

def unbounded_knapsack(p, weight_arr, value_arr, n):
    if n == 0:
        return p
    if not weight_arr:
        return p
    max_profit = 0
    for i in range(len(weight_arr)):
        if weight_arr[i] <= n:
            max_profit = max(max_profit,  unbounded_knapsack(p + value_arr[i], weight_arr, value_arr, n - weight_arr[i]))

    return max_profit


print(unbounded_knapsack(0, weight_arr=[2, 4, 6], value_arr=[5, 11, 13], n=10))