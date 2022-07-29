# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1


class Solution:

    # Function to return the diameter of a Binary Tree.
    def diameter(self ,root):

        max_val = [0]

        def dfs(root):
            nonlocal diameter
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(left + right + 1, diameter)

            return max(left, right) + 1


        diameter = 0
        dfs(root)
        return diameter