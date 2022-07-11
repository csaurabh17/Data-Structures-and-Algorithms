# Given a set of n integers, divide the set in two subsets of n/2 sizes each such that the difference of the sum of
# two subsets is as minimum as possible. If n is even, then sizes of two subsets must be strictly n/2 and if n is
# odd, then size of one subset must be (n-1)/2 and size of other subset must be (n+1)/2.
import sys

ans = ""
min_value = sys.maxsize
def solve(set1, set2, arr, n):
    global min_value
    global ans
    if len(set1) == n and len(set2) == n:
        if abs(sum(set1) - sum(set2)) < min_value:
            min_value = abs(sum(set1) - sum(set2))
            ans = "First set is : " + str(set1) + ", second set is : " + str(set2)
            return min_value
        else:
            return abs(sum(set1) - sum(set2))
    if len(set1) > n or len(set2) > n:
        return sys.maxsize

    res = min(solve(set1 + [arr[0]], set2, arr[1:], n), solve(set1, set2 + [arr[0]], arr[1:], n))
    return res


print(solve([], [], [3, 4, 5, -3, 100, 1, 89, 54, 23, 20], 5))
print(ans)
