# check if a binary tree is balanced or not


def solve(node):
    if node is None:
        return 0

    lh = solve(node.left)
    rh = solve(node.right)

    if lh == -1 or rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1

    return 1 + max(lh, rh)

