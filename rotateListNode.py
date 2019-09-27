# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        slow = head
        fast = head
        gap = 0
        while fast and gap < k:
            fast = fast.next
            gap += 1

        if not fast:
            length = gap
            k = k % length
            gap = 0
            fast = head
            while fast and gap < k:
                fast = fast.next
                gap += 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head
