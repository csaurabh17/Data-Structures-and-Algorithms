# Amazon - Chocolate distribution problem Given an array of node integers where each value represents the number of
# chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to
# distribute chocolate packets such that: Each student gets one packet. The difference between the number of
# chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.
import sys


def min_diff(arr, m):
    arr.sort()
    i = 0
    m = i + (m - 1)
    min_val = sys.maxsize
    while m < len(arr) - 1:
        min_val = min(min_val, arr[m] - arr[i])
        m += 1
        i += 1
    return min_val


print(min_diff([7, 3, 2, 4, 9, 12, 56], 3))
print(min_diff([3, 4, 1, 9, 56, 7, 9, 12], 5))
