# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        last = first = now = None
        extra = 0;
        while l1 or l2 or extra:
            l1v = l1.val if l1 != None else 0
            l2v = l2.val if l2 != None else 0
            now = ListNode(l1v + l2v + extra)
            now.next = None
            extra = 0
            if now.val >= 10:
                now.val -= 10
                extra = 1
            if last != None:
                last.next = now
            else:
                first = now
            last = now
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return first



obj = Solution()
first = ListNode(0)
#second = ListNode(8)
#first.next = second
first.next = None
#second.next = None

first1 = ListNode(0)
first1.next = None


rtn = obj.addTwoNumbers(first, first1)
print rtn.val