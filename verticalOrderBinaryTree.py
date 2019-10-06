# Definition for a binary tree node.
from collections import defaultdict, deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([(root, 0)])
        minimum = 0
        hash_set = defaultdict(list)
        while q:
            node, level = q.popleft()
            if level < minimum:
                minimum = level
            hash_set[level].append(node.val)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))

        ans = []
        level = minimum
        while level in hash_set:
            ans.append(hash_set[level])
            level += 1
        return ans
