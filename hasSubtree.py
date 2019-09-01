# -*- coding:utf-8 -*-
# in progress
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None:
            return False

        stack_1 = [pRoot1]
        stack_2 = [pRoot2]
        possible_root = []
        while stack_1:
            curr = stack_1.pop()
            if curr.val == pRoot2.val:
                possible_root.append(curr)
            while curr.left is not None:
                stack_1.append(curr.left)
                curr = curr.left
            while curr.right is not None:
                stack_1.append(curr.right)
                curr = curr.right

        if not possible_root:
            return False
        else:
            while possible_root:
                result = True
                stack_1 = [possible_root.pop()]
                stack_2 = [pRoot2]
                while stack_2 and stack_1:
                    node_1 = stack_1.pop()
                    node_2 = stack_2.pop()
                    if node_1.val != node_2.val:
                        result = False
                        break
                    while node_1.left is not None:
                        stack_1.append(node_1.left)
                        node_1 = node_1.left
                    while node_1.right is not None:
                        stack_1.append(node_1.right)
                        node_1 = node_1.right

                    while node_2.left is not None:
                        stack_2.append(node_2.left)
                        node_2 = node_2.left
                    while node_2.right is not None:
                        stack_2.append(node_2.right)
                        node_2 = node_2.right

                if result and not stack_1 and not stack_2:
                    return True

            return False
