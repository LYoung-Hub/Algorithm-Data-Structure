# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    inorder = []
    val = []

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.inorder = []
        self.DFS(root)
        for i in range(len(self.inorder) - 1, -1, -1):
            for j in range(i + 1, len(self.inorder)):
                self.inorder[i].val += self.val[j]
        return root

    def DFS(self, node):
        if not node:
            return
        self.DFS(node.left)
        self.inorder.append(node)
        self.val.append(node.val)
        self.DFS(node.right)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    solu = Solution()
    print solu.convertBST(root)
