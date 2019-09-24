# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def exist(self, idx, level, root):
        curr = root
        while level > 0:
            level_cnt = pow(2, level)
            if idx < level_cnt / 2:
                curr = curr.left
            else:
                idx -= level_cnt / 2
                curr = curr.right
            level -= 1

        return curr

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        d = 0
        curr = root
        while curr.left:
            curr = curr.left
            d += 1

        cnt = pow(2, d) - 1

        left = 0
        right = cnt

        mid = left + (right - left) / 2
        while left <= right:
            if self.exist(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
            mid = left + (right - left) / 2

        cnt += left

        return cnt


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    leftleft = TreeNode(4)
    leftright = TreeNode(5)
    rightleft = TreeNode(6)
    root.left = left
    root.right = right
    left.left = leftleft
    left.right = leftright
    right.left = rightleft
    solu = Solution()
    print solu.countNodes(root)
