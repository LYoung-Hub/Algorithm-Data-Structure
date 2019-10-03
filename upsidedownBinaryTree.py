# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.DFS(root)

    def DFS(self, node):
        if not node or not node.left:
            return node

        res = self.DFS(node.left)

        node.left.right = node
        node.left.left = node.right
        node.left = None
        node.right = None

        return res
