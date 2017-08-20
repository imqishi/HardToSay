# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            head = last = l1
            l1 = l1.next
        else:
            head = last = l2
            l2 = l2.next
        while l1 and l2:
            if l1.val < l2.val:
                last.next = l1
                last = l1
                l1 = l1.next
            else:
                last.next = l2
                last = l2
                l2 = l2.next

        if l1 is None:
            last.next = l2
        else:
            last.next = l1

        return head
obj = Solution()
head1 = ListNode(1)
head2 = ListNode(2)
a = ListNode(2)
head1.next = a
a = ListNode(3)
head2.next = a
a = ListNode(4)
head1.next.next = a
a = ListNode(7)
head2.next.next = a
head = obj.mergeTwoLists(head1, head2)
while head:
    print head.val
    head = head.next

