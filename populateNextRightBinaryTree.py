"""
# Definition for a Node.
"""
from collections import deque


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            temp = []
            for i in range(0, len(q)):
                node = q.popleft()
                temp.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(0, len(temp) - 1):
                temp[i].next = temp[i + 1]

        return root
