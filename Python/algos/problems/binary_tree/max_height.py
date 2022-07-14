# To find the maximum height of a binary tree

def solve(node):
    if node is None:
        return 0

    return 1 + max(solve(node.left), solve(node.right))