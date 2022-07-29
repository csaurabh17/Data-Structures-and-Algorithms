# for tree
#       10
#    20    30
#  7  15
from os import name


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


node = createNode(10)
node.left = createNode(20)
node.left.left = createNode(7)
node.left.right = createNode(15)

node.right = createNode(30)