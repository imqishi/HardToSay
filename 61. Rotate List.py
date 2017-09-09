# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t = head
        prev_last = None
        length = 0
        while t:
            length += 1
            if t.next is None:
                prev_last = t
            t = t.next
        
        if length <= 1 or k % length == 0:
            return head
        k = k % length
        pos = length - k
        t = head
        new_head = None
        new_tail = None
        while pos > 0:
            pos -= 1
            new_tail = t
            t = t.next
            new_head = t

        prev_last.next = head
        new_tail.next = None
        return new_head
        