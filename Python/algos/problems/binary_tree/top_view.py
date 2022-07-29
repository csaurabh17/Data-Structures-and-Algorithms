# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

import SAMPLE_INPUT_TREE_1


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):

        def leftView(root):
            if root is None:
                return
            leftView(root.left)
            print(root.val, end=" ")

        def rightView(root):
            if root is None:
                return
            print(root.val, end=" ")
            rightView(root.right)

        leftView(root)
        rightView(root.right)


Solution().topView(SAMPLE_INPUT_TREE_1.node)
