# https://leetcode.com/problems/target-sum/discuss/1470377/c-4ms-beats-98-similar-to-count-of-subset-with-given-sum-dp-explanation

matrix = [[None] * 100 for i in range(10)]


def count_subset_with_given_sum(arr, n):
    if n == 0:
        return 1
    if not len(arr) and n != 0:
        return 0
    if matrix[len(arr)][n] is not None:
        return matrix[len(arr)][n]

    count = 0
    count += count_subset_with_given_sum(arr[1:], n - arr[0]) + count_subset_with_given_sum(arr[1:], n)
    matrix[len(arr)][n] = count
    return matrix[len(arr)][n]


print(count_subset_with_given_sum([2, 3, 7, 8, 10], 13))
print(count_subset_with_given_sum([2, 3, 5, 6, 8, 10], 8))
