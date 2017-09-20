# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = None # new list's head
        t = None # record new list's last node
        n = head
        candidate = None
        count = 1

        while n is not None:
            if candidate is None: # first loop, init
                candidate = n
                count = 1
            else:
                if candidate.val == n.val: # just go next
                    count += 1
                else:
                    if count == 1: # record it
                        if h is None:
                            h = candidate
                        else:
                            t.next = candidate
                        t = candidate
                        t.next = None
                    candidate = n
                    count = 1
            n = n.next
        
        if count == 1:
            if h is None:
                h = candidate
            else:
                t.next = candidate
            if candidate is not None:
                candidate.next = None
        
        return h
            