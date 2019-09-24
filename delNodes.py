# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        if to_delete.count(root.val) == 0:
            roots = [root]
        else:
            root.val = -1
            roots = []

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                if to_delete.count(node.left.val) > 0:
                    node.left.val = -1
                    node.left = None
            if node.right:
                queue.append(node.right)
                if to_delete.count(node.right.val) > 0:
                    node.right.val = -1
                    node.right = None
            if node.val == -1:
                if node.left:
                    roots.append(node.left)
                if node.right:
                    roots.append(node.right)
                del node

        return roots
