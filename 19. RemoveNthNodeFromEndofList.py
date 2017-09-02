# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head

        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        if n > length:
            return False

        i = length - n
        p = head
        last = p
        while i > 0:
            last = p
            p = p.next
            i -= 1

        last.next = p.next

        return head

    def newRemoveNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head

        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

head = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
head.next = l1
l1.next = l2
l2.next = l3
obj = Solution()
result = obj.newRemoveNthFromEnd(head, 2)
while result:
    print result.val
    result = result.next
