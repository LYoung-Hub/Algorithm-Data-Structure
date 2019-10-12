# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow
        pre.next = None

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        dummy = ListNode(0)
        curr = dummy
        while left_sorted and right_sorted:
            if left_sorted.val < right_sorted.val:
                curr.next = left_sorted
                left_sorted = left_sorted.next
            else:
                curr.next = right_sorted
                right_sorted = right_sorted.next
            curr = curr.next
        curr.next = left_sorted or right_sorted
        return dummy.next


if __name__ == '__main__':
    head = ListNode(4)
    two = ListNode(2)
    one = ListNode(1)
    three = ListNode(3)
    head.next = two
    two.next = one
    one.next = three
    solu = Solution()
    print solu.sortList(head)
