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
        if head is None or head.next is None:
            return head
        # cut the list to 2 parts
        prev = None
        slow = fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        # sort each part
        left = self.sortList(head)
        right = self.sortList(slow)
        # merge
        return self.merge(left, right)
    
    def merge(self, left, right):
        t = ListNode(0)
        tp = t
        while left is not None and right is not None:
            if left.val < right.val:
                tp.next = left
                left = left.next
            else:
                tp.next = right
                right = right.next
            tp = tp.next
        tp.next = left if left is not None else right
        return t.next