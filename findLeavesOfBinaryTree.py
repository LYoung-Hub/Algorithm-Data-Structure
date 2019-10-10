# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        while not self.isLeaf(root):
            stack = []
            self.DFS(root, stack)
            ans.append(stack)
        ans.append([root.val])
        return ans

    def DFS(self, node, stack):
        if not node:
            return

        if self.isLeaf(node.left):
            stack.append(node.left.val)
            node.left = None
        if self.isLeaf(node.right):
            stack.append(node.right.val)
            node.right = None

        self.DFS(node.left, stack)
        self.DFS(node.right, stack)

    def isLeaf(self, node):
        if not node:
            return False
        return not node.left and not node.right


if __name__ == '__main__':
    root = TreeNode(1)
    rootleft = TreeNode(2)
    rootright = TreeNode(3)
    leftleft = TreeNode(4)
    leftright = TreeNode(5)
    root.left = rootleft
    root.right = rootright
    rootleft.left = leftleft
    rootleft.right = leftright
    solu = Solution()
    print solu.findLeaves(root)
