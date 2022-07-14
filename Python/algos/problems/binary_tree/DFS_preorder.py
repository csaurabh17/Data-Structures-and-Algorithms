# DFS pre-prder traversal of binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, new_node):
        print(new_node)
        self.pre_order(new_node.left)
        self.pre_order(new_node.right)

