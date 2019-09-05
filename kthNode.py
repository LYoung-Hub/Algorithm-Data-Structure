# -*- coding:utf-8 -*-
# 自测通过，提交不过
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode

    ans = []

    def DFS(self, root, k):
        if root is None or len(self.ans) == k:
            return

        self.DFS(root.left, k)
        if len(self.ans) < k:
            self.ans.append(root.val)
        if len(self.ans) < k:
            self.DFS(root.right, k)

    def KthNode(self, pRoot, k):
        # write code here
        if k == 0 or pRoot is None:
            return None

        self.DFS(pRoot, k)
        return self.ans[k - 1]


if __name__ == '__main__':
    root = TreeNode(8)
    left = TreeNode(6)
    right = TreeNode(10)
    root.left = left
    root.right = right
    leftleft = TreeNode(5)
    leftright = TreeNode(7)
    left.left = leftleft
    left.right = leftright
    solu = Solution()
    print solu.KthNode(root, 5)
