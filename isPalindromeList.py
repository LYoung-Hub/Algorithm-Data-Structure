# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        pre = None
        slow = fast = head
        behind = slow.next
        while fast and fast.next:
            fast = fast.next.next
            slow.next = pre
            pre = slow
            slow = behind
            behind = behind.next

        if fast:
            slow = slow.next
        while slow and pre:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    solu = Solution()
    print solu.isPalindrome(head)
