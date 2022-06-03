# https://leetcode.com/problems/target-sum/

def target_sum(up_arr, arr, n):
    if not len(arr) and sum(up_arr) == n:
        return 1
    if not len(arr) and sum(up_arr) != n:
        return 0

    count = 0

    count += target_sum(up_arr + [arr[0]], arr[1:], n) + target_sum(up_arr + [-arr[0]], arr[1:], n)
    return count


print(target_sum([], [1, 1, 2, 3], 1))
print(target_sum([], [1, 1, 1, 1, 1], 3))
