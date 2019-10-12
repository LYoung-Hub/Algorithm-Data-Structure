# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    stack = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        self.stack = []
        self.DFS(root, k)
        return self.stack[-1]

    def DFS(self, node, k):
        if not node or len(self.stack) == k:
            return

        self.DFS(node.left, k)
        if len(self.stack) < k:
            self.stack.append(node.val)
        self.DFS(node.right, k)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    solu = Solution()
    print solu.kthSmallest(root, 1)
