# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    ancestors_p = []
    ancestors_q = []

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ancestors_p = []
        self.ancestors_q = []

        self.DFS(root, [], p, q)

        while self.ancestors_q:
            n = self.ancestors_q.pop()
            if n in self.ancestors_p:
                return n

    def DFS(self, node, parents, p, q):
        if not node:
            return

        if node == p:
            self.ancestors_p = parents + [p]

        if node == q:
            self.ancestors_q = parents + [q]

        self.DFS(node.left, parents + [node], p, q)
        self.DFS(node.right, parents + [node], p, q)
