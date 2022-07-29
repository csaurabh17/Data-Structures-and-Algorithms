import SAMPLE_INPUT_TREE_1


class Solution:
    def toSumTree(self, root):
        # if root is None:
        #     return 0
        if root.left is None and root.right is None:
            prev_root = root.val
            root.val = 0
            return prev_root

        root.val = self.toSumTree(root.left) \
                   + self.toSumTree(root.right)
        return root.val


Solution().toSumTree(SAMPLE_INPUT_TREE_1.node)
