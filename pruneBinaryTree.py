# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.hasOne(root)
        return root

    def hasOne(self, node):
        if not node:
            return False
        left = self.hasOne(node.left)
        right = self.hasOne(node.right)
        if not left:
            node.left = None
        if not right:
            node.right = None
        return node.val == 1 or left or right
