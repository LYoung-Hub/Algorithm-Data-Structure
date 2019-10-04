# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    q = deque()

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q = deque()
        self.DFS(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.q.popleft().val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.q) > 0

    def DFS(self, node):
        if not node:
            return

        self.DFS(node.left)
        self.q.append(node)
        self.DFS(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
