# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.par = None
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def DFS(node, par=None):
            if node:
                node.par = par
                DFS(node.left, node)
                DFS(node.right, node)
        DFS(root)

        q = deque([(target, 0)])
        visited = {target}
        while q:
            if q[0][1] == K:
                return [node.val for node, d in q]
            node, d = q.popleft()
            for n in (node.left, node.right, node.par):
                if n and n not in visited:
                    visited.add(n)
                    q.append((n, d + 1))
        return []
