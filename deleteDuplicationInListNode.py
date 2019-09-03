# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return None
        if pHead.next is None:
            return pHead

        hashSet = {}
        p = pHead
        new_head = None
        curr = None
        while p.next is not None:
            if p.val == p.next.val:
                if p.val not in hashSet:
                    hashSet[p.val] = 1
            elif p.val not in hashSet:
                if new_head is None:
                    new_head = p
                    curr = new_head
                else:
                    curr.next = p
                    curr = curr.next
            p = p.next
        if new_head is None and p.val not in hashSet:
            new_head = p
            curr = new_head
        if new_head is not None and p.val not in hashSet:
            curr.next = p
            curr = curr.next
        if new_head is None and p.val in hashSet:
            return None
        curr.next = None

        return new_head


if __name__ == '__main__':
    head = ListNode(1)
    curr = head
    curr.next = ListNode(1)
    curr = curr.next
    curr.next = ListNode(2)
    curr = curr.next
    curr.next = ListNode(3)
    curr = curr.next
    curr.next = ListNode(3)
    curr = curr.next
    curr.next = ListNode(4)
    curr = curr.next
    curr.next = ListNode(5)
    curr = curr.next
    curr.next = ListNode(5)
    curr = curr.next

    solu = Solution()
    solu.deleteDuplication(head)
