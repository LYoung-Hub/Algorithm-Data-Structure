# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    ans = []

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTree(start, end):
            if start > end:
                return [None, ]

            trees = []
            for i in range(start, end):
                left = generateTree(start, i - 1)
                right = generateTree(i + 1, end)

                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = left
                        curr.right = right
                        trees.append(curr)
            return trees

        return generateTree(1, n) if n else 1
