# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return None
        fast = pHead.next.next
        slow = pHead.next
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            if fast.next is None or fast is None:
                return None
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
