# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    stack = []

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.stack = []
        self.DFS(root)

        for i in range(0, len(self.stack) - 1):
            self.stack[i].right = self.stack[i + 1]
            self.stack[i].left = None

        self.stack[-1].left = None
        self.stack[-1].right = None
        return root

    def DFS(self, node):
        if not node:
            return

        self.stack.append(node)
        self.DFS(node.left)
        self.DFS(node.right)
