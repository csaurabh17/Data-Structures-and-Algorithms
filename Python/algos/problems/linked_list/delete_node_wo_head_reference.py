# Given only a pointer/reference to a node to be deleted in a singly linked list, how do you delete it

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def solve(self, node):
        temp = node.value
        node.value = node.next.value
        node.next = node.next.next
        node.next.next = None
        node.next = None
        return node
