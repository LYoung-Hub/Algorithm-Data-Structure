# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None

        if pHead.next is None:
            return pHead

        q = pHead
        curr = pHead.next
        p = curr.next
        curr.next = q
        q.next = None

        while p is not None:
            q = curr
            curr = p
            p = curr.next
            curr.next = q

        return curr
