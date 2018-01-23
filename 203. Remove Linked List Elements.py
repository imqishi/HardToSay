# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(val+1)
        new_head.next = head
        last, cur = new_head, new_head.next
        while cur is not None:
            if cur.val != val:
                last = cur
                cur = cur.next
            else:
                last.next = cur.next
                if cur.next is None:
                    break
                else:
                    cur = cur.next

        return new_head.next