# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        hash_set = {}
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val in hash_set:
                return pHead1
            else:
                hash_set[pHead1.val] = 1

            if pHead2.val in hash_set:
                return pHead2
            else:
                hash_set[pHead2.val] = 1

            pHead1 = pHead1.next
            pHead2 = pHead2.next

        while pHead1 is not None:
            if pHead1.val in hash_set:
                return pHead1
            else:
                hash_set[pHead1.val] = 1
            pHead1 = pHead1.next

        while pHead2 is not None:
            if pHead2.val in hash_set:
                return pHead2
            else:
                hash_set[pHead2.val] = 1
            pHead2 = pHead2.next

        return None
