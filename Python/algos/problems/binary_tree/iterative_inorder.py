# iterative inorder traversal of binary tree
import SAMPLE_INPUT_TREE_1


def solve(root):
    if root is None:
        return

    stack = []
    res = []

    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        elif root is None:
            if len(stack) > 0:
                current_node = stack.pop()
                res.append(current_node.val)
                root = current_node.right
            else:
                return res
    return res


print(solve(SAMPLE_INPUT_TREE_1.node))
