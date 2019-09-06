# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    stack = []

    def DFS(self, root):
        if root is None:
            return

        self.DFS(root.left)
        self.stack.append(root)
        self.DFS(root.right)

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None or (pRootOfTree.left is None and pRootOfTree.right is None):
            return pRootOfTree

        self.stack = []
        self.DFS(pRootOfTree)
        self.stack[0].right = self.stack[1]
        for i in range(1, len(self.stack) - 1):
            self.stack[i].left = self.stack[i - 1]
            self.stack[i].right = self.stack[i + 1]
        self.stack[-1].left = self.stack[-2]

        return self.stack[0]
