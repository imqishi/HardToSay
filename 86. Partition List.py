# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left_h = left_t = right_h = right_t = None
        while head:
            if head.val < x:
                if left_h is None:
                    left_h = head
                else:
                    left_t.next = head
                left_t = head
            else:
                if right_h is None:
                    right_h = head
                else:
                    right_t.next = head
                right_t = head

            head = head.next
        
        if left_h is not None:
            left_t.next = right_h
            if right_h is not None:
                right_t.next = None
            return left_h
        else:
            if right_h is not None:
                right_t.next = None
            return right_h