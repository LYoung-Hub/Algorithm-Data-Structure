"""
# Definition for a Node.
"""


class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        original = head
        while original:
            clone = Node(original.val, original.next, None)
            original.next = clone
            original = clone.next

        original = head
        while original:
            clone = original.next
            clone.random = original.random.next
            original = clone.next

        original = head
        clone_head = head.next
        clone = head.next
        while original:
            original.next = clone.next
            clone.next = original.next.next
            original = original.next
            clone = clone.next

        return clone_head
