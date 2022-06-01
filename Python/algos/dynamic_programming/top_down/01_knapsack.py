# solving 0 1 knapsack using top down approach DP
# w= [1, 4 ,5 ,7] v= [1, 3, 4, 5], size = 7

def find_max(weight_matrix, value_matrix, w):
    n = len(weight_matrix)
    matrix = [[None] * (w + 1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            else:
                if weight_matrix[i - 1] <= j:
                    matrix[i][j] = max(weight_matrix[i - 1] + matrix[i - 1][j - weight_matrix[i - 1]],
                                       matrix[i - 1][j])
                else:
                    matrix[i][j] = matrix[i - 1][j]

    return matrix[n][w]


print(find_max([1, 4, 5, 7], [1, 3, 4, 5], 14))
