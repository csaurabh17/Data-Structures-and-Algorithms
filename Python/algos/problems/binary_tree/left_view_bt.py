# https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1

"""
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
level_arr = []
class Solution:
    # Function to return list containing elements of right view of binary tree.
    def rightView(self ,root):
        self.solve(root, 0)
        return level_arr

    def solve(self, root, level):
        if not root or root == 'N':
            return
        if len(level_arr) == level:
            level_arr.append(root.data)

        self.solve(root.right, level + 1)
        self.solve(root.left, level + 1)