# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next or m == n:
            return head

        pre = None
        curr = head
        behind = curr.next
        i = 1
        while i < m:
            pre = curr
            curr = curr.next
            behind = curr.next
            i += 1

        mid_head = curr
        while i < n:
            mid_head.next = behind.next
            behind.next = curr
            curr = behind
            behind = mid_head.next
            i += 1

        mid_head.next = behind
        if pre:
            pre.next = curr
        else:
            return curr

        return head


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(5)
    solu = Solution()
    print solu.reverseBetween(head, 1, 2)
