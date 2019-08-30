# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None and pHead2 is None:
            return None
        elif pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        else:
            if pHead1.val <= pHead2.val:
                head = pHead1
                pHead1 = pHead1.next
            else:
                head = pHead2
                pHead2 = pHead2.next

            curr = head
            while pHead1 is not None and pHead2 is not None:
                if pHead1.val <= pHead2.val:
                    curr.next = pHead1
                    pHead1 = pHead1.next
                else:
                    curr.next = pHead2
                    pHead2 = pHead2.next
                curr = curr.next

            if pHead1 is not None:
                curr.next = pHead1

            if pHead2 is not None:
                curr.next = pHead2

            return head
