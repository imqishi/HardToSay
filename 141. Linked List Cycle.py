# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = slow = head
        while fast is not None and slow is not None:
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
            if fast == slow:
                return True

        return False

a = ListNode(1)
b = ListNode(2)
a.next = b
b.next = a
obj = Solution()
print obj.hasCycle(a)