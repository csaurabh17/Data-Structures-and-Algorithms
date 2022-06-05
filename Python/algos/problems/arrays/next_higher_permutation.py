# https://leetcode.com/problems/next-permutation/

import sys


class Solution:
    def nextPermutation(self, nums) -> None:
        # if you want to print permutations return self.permute([], nums)
        start = -1
        end = -1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                start = i
                break

        if start == -1:
            nums.sort()
            return nums

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[start]:
                nums = self.swap(nums, i, start)
                break

        return nums[:start + 1] + self.reverse(nums[start + 1:], start + 1, len(nums[start + 1:]) - 1)

    @staticmethod
    def swap(nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums

    def reverse(self, nums, i, j):
        while i < j:
            self.swap(nums, i, j)
        return nums
    # just to print permutations
    # def permute(self, processed, nums):
    #     if not nums:
    #         print(processed, "::", nums)
    #         return
    #
    #     c = nums[0]
    #
    #     for i in range(len(nums) + 1):
    #         f = processed[:i]
    #         l = processed[i:]
    #         self.permute(f + [c] + l, nums[1:])


print(Solution().nextPermutation([3, 2, 1]))
print(Solution().nextPermutation([1, 2]))
print(Solution().nextPermutation([1, 3, 4, 5, 2]))
