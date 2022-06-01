# Google question -https://leetcode.com/discuss/interview-question/1279773/google-interview-question-array-subset-sum
# -equals-k

# [2, 3, 7, 8, 10], 9
def subset_sum(arr, total):
    n = len(arr)
    matrix = [[None] * (total + 1) for i in range(n + 1)]

    if matrix[n][total] is not None:
        return matrix[n][total]

    for i in range(n + 1):
        for j in range(total + 1):
            if j != 0 and i == 0:
                matrix[i][j] = False
            if j == 0:
                matrix[i][j] = True
            else:
                if arr[i - 1] <= j:
                    matrix[i][j] = matrix[i - 1][j - arr[i - 1]] or matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j]
    return matrix[n][total]


print(subset_sum([2, 3, 7, 8, 10], 10))
