# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left_most = []
        leaves = []
        right_most = []

        def findLeft(node):
            if not node:
                return
            left_most.append(node)
            if node.left:
                findLeft(node.left)
            else:
                findLeft(node.right)
        left_most.append(root)
        if root.left:
            findLeft(root.left)

        def findLeaves(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node)
                return
            findLeaves(node.left)
            findLeaves(node.right)
        findLeaves(root)

        def findRight(node):
            if not node:
                return

            right_most.append(node)
            if not node.right:
                findRight(node.left)
            else:
                findRight(node.right)
        right_most.append(root)
        if root.right:
            findRight(root.right)

        hash_set = {}
        ans = []
        for l in left_most:
            hash_set[l] = 1
            ans.append(l.val)

        for le in leaves:
            if le not in hash_set:
                hash_set[le] = 1
                ans.append(le.val)

        while right_most:
            r = right_most.pop()
            if r not in hash_set:
                hash_set[r] = 1
                ans.append(r.val)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    rootleft = TreeNode(2)
    rootright = TreeNode(9)
    leftleft = TreeNode(3)
    rightleft = TreeNode(5)
    rightright = TreeNode(8)
    leftleftleft = TreeNode(4)
    rightleftleft = TreeNode(6)
    rightleftright = TreeNode(7)
    root.left = rootleft
    root.right = rootright
    rootleft.left = leftleft
    rootright.left = rightleft
    rootright.right = rightright
    leftleft.left = leftleftleft
    rightright.left = rightleftleft
    rightright.right = rightleftright
    solu = Solution()
    print solu.boundaryOfBinaryTree(root)
