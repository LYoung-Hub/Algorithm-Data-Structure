# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None

        p = head
        q = head
        while q is not None and k > 0:
            k -= 1
            q = q.next

        if k > 0:
            return None

        while q is not None:
            p = p.next
            q = q.next

        return p
