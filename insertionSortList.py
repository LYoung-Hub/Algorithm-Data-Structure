# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode('-Inf')
        dummy.next = head
        sorted_end = dummy.next
        inner = dummy.next
        while sorted_end.next:
            curr = sorted_end.next
            sorted_end.next = curr.next

            if inner.val > curr.val:
                inner = dummy

            while inner != sorted_end and inner.next.val < curr.val:
                inner = inner.next

            curr.next = inner.next
            inner.next = curr

            if inner == sorted_end:
                sorted_end = curr

        return dummy.next


if __name__ == '__main__':
    four = ListNode(4)
    two = ListNode(2)
    one = ListNode(1)
    three = ListNode(3)
    four.next = two
    two.next = one
    one.next = three
    solu = Solution()
    print solu.insertionSortList(four)
