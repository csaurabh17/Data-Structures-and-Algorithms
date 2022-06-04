# https://leetcode.com/problems/maximum-subarray/
import sys


class Solution:
    def maxSubArray(self, nums) -> int:
        total = 0
        max_value = - sys.maxsize - 1
        for i in range(len(nums)):
            total = total + nums[i]
            if total > max_value:
                max_value = total
            if total < 0:
                total = 0
        return max_value


a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
