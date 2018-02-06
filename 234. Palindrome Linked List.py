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
        if head is None or head.next is None:
            return True

        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # this means has even nums
        if fast is not None:
            slow = slow.next
        
        # reverse left linked list
        last = new_head = ListNode(1)
        cur = new_head.next = head
        while cur != slow:
            t = cur.next
            cur.next = last
            last = cur
            cur = t

        # this is important
        if fast is None:
            cur = last
        else:
            cur = last.next
        # compare
        while slow is not None:
            if slow.val != cur.val:
                return False
            slow = slow.next
            cur = cur.next

        return True

a = ListNode(1)
b = ListNode(2)
c = ListNode(1)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
#d.next = e
obj = Solution()
print obj.isPalindrome(a)