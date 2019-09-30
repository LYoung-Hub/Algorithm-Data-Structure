# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left = self.DFS(root.left)
        right = self.DFS(root.right)
        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def DFS(self, node):
        if not node:
            return 0

        return max(self.DFS(node.left), self.DFS(node.right)) + 1
