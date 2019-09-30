# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        fast = head.next
        slow = head
        pre = None
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next

        mid = slow
        if pre:
            pre.next = None

        root = TreeNode(mid.val)
        if head == mid:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
