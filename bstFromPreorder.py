# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return
        root = TreeNode(preorder[0])
        idx = 1
        while idx < len(preorder) and preorder[idx] < root.val:
            idx += 1
        root.left = self.bstFromPreorder(preorder[1:idx])
        root.right = self.bstFromPreorder(preorder[idx:])
        return root


if __name__ == '__main__':
    solu = Solution()
    print solu.bstFromPreorder([8,5,1,7,10,12])
