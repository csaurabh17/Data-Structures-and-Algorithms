# https://leetcode.com/problems/top-k-frequent-elements/

import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        h, res = [], []
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        for i in freq_dict:
            heapq.heappush(h, (freq_dict[i], i))
            if len(h) > k:
                heapq.heappop(h)

        for i in reversed(range(len(h))):
            res.append(h[i][1])
        return res


print(solve([1, 1, 1, 3, 2, 2, 4], 2))
