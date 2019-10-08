# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        stack = [s]
        while stack:
            curr = stack.pop()
            if self.isSameTree(curr, t):
                return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False

    def isSameTree(self, s, t):
        if not s and not t:
            return True

        if not s or not t:
            return False

        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
