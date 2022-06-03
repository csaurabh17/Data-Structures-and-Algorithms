# solving 0 1 knapsack using top down approach DP
# w= [1, 4 ,5 ,7] v= [1, 3, 4, 5], size = 7


def find_max(final_arr, w_arr, v_arr, n):
    ln = len(w_arr)
    t = [[None] * (n + 1) for i in range(ln + 1)]
    for i in range(ln + 1):
        for j in range(n + 1):
            if j == 0:
                t[i][j] = 1
            elif i == 0 and j != 0:
                t[i][j] = 0
            else:
                if sum(final_arr) + w_arr[i - 1] <= j:
                    t[i][j] = max(v_arr[0] + t[i - 1][n], t[i - 1][j])
                else:
                    t[i][j] = t[i-1][j]
    return t[ln][n]


print(find_max([], [1, 4, 5, 7], [1, 3, 4, 5], 14))
