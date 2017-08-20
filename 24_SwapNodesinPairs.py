# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # while list node is short than 2...
        if head is None or head.next is None:
            return head
        # get new head
        head = head.next
        last = head
        cur = head.next
        next = cur.next

        while next:
            cur.next = last
            if next.next is not None:
                last.next = next.next
                last = next
                cur = next.next
                next = cur.next
            else:
                last.next = next
                break

        # in this situation, list node length is even, it will lost one item
        if next is None:
            cur.next = last
            last.next = None

        return head

    def swapPairsByRecursion(self, head):
        if head is None or head.next is None:
            return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n


obj = Solution()
head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
#head.next = a
#a.next = b
#b.next = c
#c.next = d
head = obj.swapPairs(head)
while head:
    print head.val
    head = head.next
