"""
# Definition for a Node.
"""


class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    seq = []

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root

        self.seq = []
        self.DFS(root)

        for i in range(1, len(self.seq) - 1):
            self.seq[i].left = self.seq[i - 1]
            self.seq[i].right = self.seq[i + 1]

        self.seq[0].right = self.seq[1]
        self.seq[0].left = self.seq[-1]
        self.seq[-1].left = self.seq[-2]
        self.seq[-1].right = self.seq[0]

        return self.seq[0]

    def DFS(self, node):
        if not node:
            return

        self.DFS(node.left)
        self.seq.append(node)
        self.DFS(node.right)
