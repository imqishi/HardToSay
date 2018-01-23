# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        last, cur = head, head.next
        while cur is not None:
            newer = cur.next
            cur.next = last
            last = cur
            cur = newer

        head.next = None
        
        return last

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
obj = Solution()
t = obj.reverseList(a)
print t.next.next.next.next