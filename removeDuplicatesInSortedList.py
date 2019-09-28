# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if not head.next:
            return head

        new_head = left = right = head

        while right:
            right = right.next
            while right and right.val == left.val:
                right = right.next

            left.next = right
            left = right

        return new_head
