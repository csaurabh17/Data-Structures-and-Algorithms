# level order traversal of binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def level_order(self, new_node):
        queue = []
        result = []
        queue.append(new_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
