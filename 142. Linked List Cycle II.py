# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fast = slow = head
        has = False
        while fast is not None and slow is not None:
            slow = slow.next
            if fast.next is None:
                break
            fast = fast.next.next
            if fast == slow:
                has = True
                break

        if has is False:
            return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return fast

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = d
obj = Solution()
print obj.detectCycle(a).val