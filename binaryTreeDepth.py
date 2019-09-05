# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def DFS(self, root, depth):
        if root is None:
            return depth

        depth += 1
        left_depth = self.DFS(root.left, depth)
        right_depth = self.DFS(root.right, depth)

        depth = max(left_depth, right_depth)

        return depth

    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0

        return self.DFS(pRoot, 0)


