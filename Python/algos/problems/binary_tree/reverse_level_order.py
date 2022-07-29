"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


def reverseLevelOrder(root):
    queue = []
    stack = []

    queue.append(root)

    while len(queue) > 0:
        current_node = queue.pop(0)
        stack.insert(0, current_node.data)

        if current_node.right:
            queue.append(current_node.right)
        if current_node.left:
            queue.append(current_node.left)

    return stack