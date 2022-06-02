# solving equal sum partition problem
# [1,5,5,11,5]

matrix = [[None] * 100 for i in range(10)]


def subset_sum_without_looping(arr, n):
    if n == 0:
        return True
    if not len(arr) and n != 0:
        return False
    if matrix[len(arr)][n] is not None:
        return matrix[len(arr)][n]

    matrix[len(arr)][n] = subset_sum_without_looping(arr[1:], n - arr[0]) or subset_sum_without_looping(arr[1:], n)
    return matrix[len(arr)][n]


def equal_sum(arr):
    total_sum = sum(arr)
    return subset_sum_without_looping(arr, int(total_sum / 2)) if total_sum % 2 == 0 else False


print(equal_sum([2, 5, 3, 3, 1]))
print(equal_sum([1, 5, 5, 11]))
print(equal_sum([1, 2, 3, 5]))
