# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    ans = None
    curr_max = float('Inf')

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.ans = None
        self.curr_max = float('Inf')
        self.DFS(root, p)
        return self.ans

    def DFS(self, node, p):
        if not node:
            return

        if node.val > p.val:
            if node.val < self.curr_max:
                self.curr_max = node.val
                self.ans = node
            self.DFS(node.left, p)
        else:
            self.DFS(node.right, p)
