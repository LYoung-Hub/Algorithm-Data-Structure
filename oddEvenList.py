# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        odd_curr = odd = head.next
        even_curr = even = head
        curr = head.next.next
        even.next = None
        odd.next = None
        flag = 1
        while curr:
            if flag == 1:
                even_curr.next = curr
                even_curr = even_curr.next
            else:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            flag = -1 * flag
            curr = curr.next
        even_curr.next = odd
        odd_curr.next = None
        return even


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solu = Solution()
    print solu.oddEvenList(head)
