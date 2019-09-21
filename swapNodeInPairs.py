# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node_one = head
        node_two = head.next

        node_one.next = node_two.next
        node_two.next = node_one
        node_one, node_two = node_two, node_one
        result_head = node_one
        curr_father = node_two

        while node_two.next and node_two.next.next:
            node_one = node_one.next.next
            node_two = node_two.next.next
            node_one.next = node_two.next
            node_two.next = node_one
            curr_father.next = node_two
            node_one, node_two = node_two, node_one
            curr_father = node_two

        return result_head
