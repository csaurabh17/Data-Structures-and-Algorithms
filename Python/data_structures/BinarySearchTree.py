class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                temp = temp.right
                return True

    def contains(self, value):
        if self.root is None:
            return False
        new_node = Node(value)
        temp = self.root
        while temp is not None:
            if temp.value == new_node.value:
                return True
            elif new_node.value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def min_value_node(self, temp):
        while temp.left is not None:
            temp = temp.left
        return temp.value

    def bfs(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

# Instantiating
bst = BinarySearchTree()
# print(bst.root)

# inserting
bst.insert(1)
# print(bst.root.value)
bst.insert(2)
# print(bst.root.right.value)
bst.insert(0)
# print(bst.root.left.value)

# contains
# print(bst.contains(0))

# min value
# print(bst.min_value_node(bst.root))

# bfs traversal
print(bst.bfs())
