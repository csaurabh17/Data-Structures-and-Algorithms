# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = head
        j = head
        while i and j:
            if i is None or j.next is None:
                return False
            if i == j:
                return True
            i = i.next
            j = j.next.next

        return False
