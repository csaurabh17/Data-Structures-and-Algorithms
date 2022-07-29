# https://www.geeksforgeeks.org/create-a-mirror-tree-from-the-given-binary-tree/

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


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def mirror_tree(root, mirror=None):
    if root is None:
        return
    mirror = createNode(root.val)
    mirror.right = mirror_tree(root.left, mirror.right)
    mirror.left = mirror_tree(root.right, mirror.left)
    return mirror


node = createNode(5)
node.left = createNode(3)
node.left.left = createNode(2)
node.left.right = createNode(4)

node.right = createNode(6)


inorder(mirror_tree(node))
