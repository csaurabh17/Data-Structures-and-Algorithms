# solving 0 1 knapsack using top down approach DP
# w= [1, 4 ,5 ,7] v= [1, 3, 4, 5], size = 7

def find_max(weight_matrix, value_matrix, w):
    n = len(weight_matrix)
    matrix = [[None] * (w + 1) for i in range(n + 1)]

    return matrix


print(find_max([1, 4, 5, 7], [1, 3, 4, 5], 7))
