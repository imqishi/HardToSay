# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is not None and head.next is not None:
            # get middle pos
            first = second = head
            left_end = None
            while second is not None:
                left_end = first
                first = first.next
                if second.next is not None:
                    second = second.next.next
                else:
                    break
            left_end.next = None
            middle = first

            # reverse second part
            right_end = last = middle
            now = last.next
            while now is not None:
                t = now.next
                now.next = last
                last = now
                now = t
            right_start = last
            right_end.next = None
            
            # construct
            left_start = head
            while left_start is not None and right_start is not None:
                left_bak = left_start.next
                right_bak = right_start.next
                left_start.next = right_start
                left_start = left_bak
                right_start.next = left_start
                right_start = right_bak
        

    
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
obj = Solution()
obj.reorderList(a)