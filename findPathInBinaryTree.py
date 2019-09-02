# -*- coding:utf-8 -*-
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径

    ans = []

    def DFS(self, root, path, expectNumber):
        if root.left is None and root.right is None:
            if expectNumber == root.val:
                path.append(root.val)
                valid_path = copy.deepcopy(path)
                self.ans.append(valid_path)
                path.pop()
        else:
            path.append(root.val)
            self.DFS(root.left, path, expectNumber - root.val)
            self.DFS(root.right, path, expectNumber - root.val)
            path.pop()

    def FindPath(self, root, expectNumber):
        # write code here
        path = []
        self.DFS(root, path, expectNumber)

        return self.ans


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(12)
    leftleft = TreeNode(4)
    rightright = TreeNode(7)
    root.left = left
    root.right = right
    left.left = leftleft
    left.right = rightright
    solu.FindPath(root, 15)
