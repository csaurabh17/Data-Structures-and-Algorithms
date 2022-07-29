# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root and subRoot or (root and not subRoot):
            return False
        if self.check_subtree(root, subRoot):
            return True

        return self.check_subtree(root.left, subRoot) or self.check_subtree(root.right, subRoot)

    def check_subtree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root and subRoot or (root and not subRoot):
            return False
        if root.val != subRoot.val:
            return False
        return self.check_subtree(root.left, subRoot.left) and self.check_subtree(root.right, subRoot.right)
        return True


root_elem = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subroot_elem = TreeNode(4, TreeNode(1), TreeNode(2))

print(Solution().isSubtree(root_elem, subroot_elem))