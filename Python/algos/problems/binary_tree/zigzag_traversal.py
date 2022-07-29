


class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root, level=0):
        if not root:
            return
        queue = []
        res = []
        queue.append(root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            res.append(current_node.data)
            level = 0 if 1 else 1
            if level == 1:
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
            elif level == 0:
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return res


#
# root_elem = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
# subroot_elem = TreeNode(4, TreeNode(1), TreeNode(2))
#
# print(Solution().isSubtree(root_elem, subroot_elem))