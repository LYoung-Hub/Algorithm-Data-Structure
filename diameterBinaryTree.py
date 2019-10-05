# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    ans = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ans = 0
        self.depth(root)
        return self.ans - 1

    def depth(self, node):
        if not node:
            return 0
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        if left_depth + right_depth + 1 > self.ans:
            self.ans = left_depth + right_depth + 1
        return max(left_depth, right_depth) + 1
