# Iterative pre-order traversal of binary tree

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


def solve(root):
    if root is None:
        return

    stack = []
    res = []
    stack.append(root)
    while len(stack) > 0:
        current_node = stack.pop()
        res.append(current_node.val)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    return res


node = createNode(10)
node.left = createNode(20)
node.left.left = createNode(10)
node.left.right = createNode(15)

node.right = createNode(30)
print(solve(node))