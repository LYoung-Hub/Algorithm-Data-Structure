# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return

        new_right = self.Mirror(root.left)
        new_left = self.Mirror(root.right)
        root.left = new_left
        root.right = new_right

        return root
