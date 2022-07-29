import SAMPLE_INPUT_TREE_1
import DFS_inorder


def solve(s):
    arr = []
    if not s:
        return None
    root = SAMPLE_INPUT_TREE_1.createNode(s[0])
    if len(s) <= 1:
        return root
    left_start_index = s.find("(")
    arr.append(s[left_start_index])
    i = 0
    for i in range(left_start_index + 1, len(s)):
        if s[i] == "(":
            arr.append(s[i])
        elif s[i] == ")":
            arr.pop()
        if len(arr) <= 0:
            break

    root.left = solve(s[left_start_index + 1:i])
    root.right = solve(s[i + 2:len(s) - 1])
    return root


root = solve("4(2(3)(1))(6(5))")
print(root)