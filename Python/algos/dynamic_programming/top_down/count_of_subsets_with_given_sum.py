# https://leetcode.com/problems/target-sum/discuss/1470377/c-4ms-beats-98-similar-to-count-of-subset-with-given-sum-dp-explanation

def count_subset_with_given_sum(arr, total):
    n = len(arr)
    matrix = [[None] * (total + 1) for i in range(n + 1)]

    if matrix[n][total] is not None:
        return matrix[n][total]

    for i in range(n + 1):
        for j in range(total + 1):
            if j != 0 and i == 0:
                matrix[i][j] = 0
            if j == 0:
                matrix[i][j] = 1
            else:
                if arr[i - 1] <= j:
                    matrix[i][j] = matrix[i - 1][j - arr[i - 1]] + matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j]


print(count_subset_with_given_sum([2, 3, 7, 8, 10], 13))
print(count_subset_with_given_sum([2, 3, 5, 6, 8, 10], 10))
