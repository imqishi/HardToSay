# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p = head
        if p is None or p.next is None or m == n:
            return p

        i = 1
        # find left1
        if m == 1:
            left1 = None
            l = p
        else:
            while i < m - 1:
                i += 1
                p = p.next
            left1 = p
            l = p = p.next
            i += 1
        # notice that p.next must not be none because if that true m will equal to n
        p = p.next
        while i < n:
            t = p.next
            p.next = l
            l = p
            p = t
            i += 1

        if left1 is not None:
            left1.next.next = p
            left1.next = l
        else:
            head.next = p
            head = l
        
        p = head
        while p:
            print p.val
            p = p.next

a1 = ListNode(1)
a2 = ListNode(2)
a1.next = a2
obj = Solution()
obj.reverseBetween(a1,1,2)