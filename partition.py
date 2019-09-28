# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        if not head.next:
            return head

        curr = head
        pre = None
        after = None
        l1 = None
        l2 = None
        while curr:
            if curr.val < x:
                if not pre:
                    l1 = curr
                    pre = l1
                else:
                    pre.next = curr
                    pre = pre.next
            else:
                if not after:
                    l2 = curr
                    after = l2
                else:
                    after.next = curr
                    after = after.next

            curr = curr.next

        if after:
            after.next = None
        if not l1:
            return l2
        else:
            if l2:
                pre.next = l2
            else:
                pre.next = None

        return l1


if __name__ == '__main__':
    one = ListNode(1)
    two = ListNode(4)
    three = ListNode(3)
    four = ListNode(2)
    five = ListNode(5)
    six = ListNode(2)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    solu = Solution()
    print solu.partition(one, 3)
