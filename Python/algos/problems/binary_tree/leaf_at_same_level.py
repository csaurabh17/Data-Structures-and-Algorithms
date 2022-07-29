# https://practice.geeksforgeeks.org/problems/leaf-at-same-level/1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def createNode(val):
    newNode = Node(0)
    newNode.val = val
    newNode.left = None
    newNode.right = None
    return newNode


leaf_level = 0


def check(root, level=0):
    global leaf_level
    if root is None:
        return True
    if root.left is None and root.right is None:
        if leaf_level == 0:
            leaf_level = level
            return True
        return leaf_level == level

    return check(root.left, level + 1) and check(root.right, level + 1)


node = createNode(10)
node.left = createNode(20)
node.left.left = createNode(10)
node.left.right = createNode(15)

node.right = createNode(30)
print(check(node))
