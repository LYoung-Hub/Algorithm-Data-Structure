# -*- coding:utf-8 -*-
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        queue = deque()
        queue.append(pRoot)
        ans = []
        direction = 1
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
            if direction == -1:
                temp.reverse()
            direction = direction * -1
            ans.append(temp)

        return ans


if __name__ == '__main__':
    root = TreeNode(8)
    left = TreeNode(10)
    right = TreeNode(6)
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
