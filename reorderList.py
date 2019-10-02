# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tail_head = slow.next
        slow.next = None
        curr = tail_head
        pre = None
        while curr:
            behind = curr.next
            curr.next = pre
            pre = curr
            curr = behind

        tail_head = pre
        curr = head
        while tail_head and curr:
            old = curr.next
            new = tail_head.next
            curr.next = tail_head
            curr = old
            tail_head.next = curr
            tail_head = new


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solu = Solution()
    print solu.reorderList(head)
