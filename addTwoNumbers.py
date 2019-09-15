# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == 0 and l1.next is None:
            return l2

        if l2 == 0 and l2.next is None:
            return l1

        head = ListNode(0)
        curr = head
        c = 0
        while l1 and l2:
            value = (l1.val + l2.val + c) % 10
            c = (l1.val + l2.val + c) / 10

            node = ListNode(value)
            curr.next = node
            curr = node

            l1 = l1.next
            l2 = l2.next

        if c == 0:
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return head.next

        while l1:
            value = (l1.val + c) % 10
            c = (l1.val + c) / 10

            node = ListNode(value)
            curr.next = node
            curr = node

            l1 = l1.next

        while l2:
            value = (l2.val + c) % 10
            c = (l2.val + c) / 10

            node = ListNode(value)
            curr.next = node
            curr = node

            l2 = l2.next

        if c == 1:
            node = ListNode(1)
            curr.next = node

        return head.next


if __name__ == '__main__':
    l1 = ListNode(3)
    l1.next = ListNode(7)

    l2 = ListNode(9)
    l2.next = ListNode(2)

    solu = Solution()
    solu.addTwoNumbers(l1, l2)
