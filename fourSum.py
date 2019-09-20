# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        for i in range(0, n):
            fast = fast.next

        if not fast:
            new_head = head.next
            del head
            return new_head

        while fast.next:
            slow = slow.next
            fast = fast.next

        node = slow.next
        slow.next = slow.next.next
        del node

        return head
