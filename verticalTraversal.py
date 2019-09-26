from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    loc = defaultdict(lambda: defaultdict(list))

    def DFS(self, node, x, y):
        if not node:
            return

        self.loc[x][y].append(node.val)
        self.DFS(node.left, x - 1, y + 1)
        self.DFS(node.right, x + 1, y + 1)

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.loc = defaultdict(lambda: defaultdict(list))
        self.DFS(root, 0, 0)

        ans = []
        for x in sorted(self.loc):
            vertical = self.loc[x]
            curr = []
            for y in sorted(vertical):
                curr.extend(sorted(vertical[y]))
            ans.append(curr)

        return ans
