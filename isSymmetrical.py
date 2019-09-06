# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isSame(self, left, right):
        if not left and not right:
            return True

        if (left and right) and left.val == right.val:
            return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)

        return False

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True

        if (pRoot.left and not pRoot.right) or (pRoot.right and not pRoot.left):
            return False

        return self.isSame(pRoot.left, pRoot.right)


if __name__ == '__main__':
    root = TreeNode(8)
    left = TreeNode(6)
    right = TreeNode(6)
    root.left = left
    root.right = right
    leftleft = TreeNode(5)
    leftright = TreeNode(7)
    left.left = leftleft
    left.right = leftright
    rightleft = TreeNode(7)
    rightright = TreeNode(5)
    right.left = rightleft
    right.right = rightright
    solu = Solution()
    print solu.isSymmetrical(root)
