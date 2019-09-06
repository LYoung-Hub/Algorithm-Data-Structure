# -*- coding:utf-8 -*-
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        queue = deque()
        queue.append(pRoot)
        ans = []
        while queue:
            length = len(queue)
            temp = []
            for i in range(0, length):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)

        return ans


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
    rightleft = TreeNode(9)
    rightright = TreeNode(11)
    right.left = rightleft
    right.right = rightright
    solu = Solution()
    print solu.Print(root)
