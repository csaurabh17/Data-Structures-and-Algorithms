# Solving 0-1 Knapsack
# [1, 3, 4, 5] - [1, 4, 5, 7] - Knapsack weight is 7

# with memoization - assuming node constraint is 100 and size is 1000
t = [[-1] * 200 for i in range(200)]


def find_max_profit(final_arr, w_arr, v_arr, n):
    if not w_arr:
        return sum(final_arr)
    if sum(final_arr) + w_arr[0] > n:
        return sum(final_arr)

    if t[len(w_arr)][n] != -1:
        return t[len(w_arr)][n]

    t[len(w_arr)][n] = max(find_max_profit(final_arr + [v_arr[0]], w_arr[1:], v_arr[1:], n),
                           find_max_profit(final_arr, w_arr[1:], v_arr[1:], n))
    return t[len(w_arr)][n]


print(find_max_profit([], [1, 4, 5, 7], [1, 3, 4, 5], 14))
print(find_max_profit([], [10, 20, 30], [60, 100, 120], 50))
print(find_max_profit([], [3, 4, 6, 5], [2, 3, 1, 4], 8))
