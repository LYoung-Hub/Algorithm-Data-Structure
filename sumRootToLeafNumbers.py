# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    numbers = []

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.numbers = []
        self.DFS(root, 0)
        return sum(self.numbers)

    def DFS(self, node, number):
        if not node:
            return 
        if not node.left and not node.right:
            number = number * 10 + node.val
            self.numbers.append(number)
            return

        self.DFS(node.left, number * 10 + node.val)
        self.DFS(node.right, number * 10 + node.val)
