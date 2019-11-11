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
        if not root:
            return True

        inorder = []

        def DFS(node):
            if not node:
                return
            DFS(node.left)
            inorder.append(node.val)
            DFS(node.right)

        for i in range(0, len(inorder) - 1):
            if inorder[i] > inorder[i + 1]:
                return False
        return True


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    solu = Solution()
    print solu.isValidBST(root)
