# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    root = None

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        self.DFS(nums, [])
        return self.root

    def DFS(self, nums, stack):
        length = len(nums)
        if length == 0:
            return

        mid = length / 2
        node = TreeNode(nums[mid])
        if not stack:
            stack.append(node)
            self.root = node
        else:
            root = stack[-1]
            if node.val < root.val:
                root.left = node
            else:
                root.right = node

        self.DFS(nums[:mid], stack + [node])
        self.DFS(nums[mid + 1:], stack + [node])
