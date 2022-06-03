# solving 0 1 knapsack using top down approach DP
# w= [1, 4 ,5 ,7] v= [1, 3, 4, 5], size = 7

t = [[-1] * 200 for i in range(200)]


def cut_rod(final_arr, w_arr, n):
    if n <= 0:
        return sum(final_arr)
    if not w_arr:
        return sum(final_arr)

    for i in range(n):
        if i <= n:
            return max(cut_rod(final_arr + [w_arr[i]], w_arr, n - w_arr[i]),
                       cut_rod(final_arr, w_arr[1:], n))


# print(cut_rod([], [1, 5, 8, 9, 10, 17, 17, 20], [1, 2, 3, 4, 5, 6, 7, 8], 14))
print(cut_rod([], [2, 5, 7, 8, 10], 5))
