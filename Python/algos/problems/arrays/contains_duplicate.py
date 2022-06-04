# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums_map = {"2": "d"}
        for i in range(len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = 0
            else:
                return True
        return False


a = Solution()
print(a.containsDuplicate([1, 1, 2, 3, 4]))
