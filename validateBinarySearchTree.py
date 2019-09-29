# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.DFS(root, float('-Inf'), float('Inf'))

    def DFS(self, node, low, high):
        if not node:
            return True

        if not low < node.val < high:
            return False

        return self.DFS(node.left, low, node.val) and self.DFS(node.right, node.val, high)


if __name__ == '__main__':
    root = TreeNode(10)
    rootleft = TreeNode(5)
    rootright = TreeNode(15)
    rightleft = TreeNode(6)
    rightright = TreeNode(20)
    root.left = rootleft
    root.right = rootright
    root.right.left = rightleft
    root.right.right = rightright
    solu = Solution()
    print solu.isValidBST(root)
