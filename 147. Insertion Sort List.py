# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        cur = head
        while cur is not None:
            newPtr = ListNode(cur.val)
            insertPos = self.findPos(newHead, cur.val)
            newPtr.next = insertPos.next
            insertPos.next = newPtr
            cur = cur.next
        
        return newHead.next
    
    def findPos(self, head, val):
        while head.next is not None:
            if head.next.val > val:
                return head
            head = head.next
        return head

a = ListNode(4)
b = ListNode(3)
c = ListNode(2)
a.next = b
b.next = c
obj = Solution()
rtn = obj.insertionSortList(a)
print rtn.val