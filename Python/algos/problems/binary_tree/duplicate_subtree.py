
# User function Template for python3
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def dupSub(self, root):
        if root is None:
            return 0
        m = {}
        def solve(root):
            if not root:
                return "$"
            if not root.left and not root.right:
                return root.data
            # if not root.left or not root.right:
            #     return "$"

            s = str(root.data)
            s = s + str(solve(root.left)) + str(solve(root.right))
            if s in m:
                m[s] = m[s] + 1
            else:
                m[s] = 0
            return s

        solve(root)
        for k in m:
            # print(k,m[k])
            if m[k] > 0:
                return 1
        return 0