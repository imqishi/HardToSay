# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        mapper = {}
        phead = None
        ptail = None
        while head is not None:
            if head in mapper:
                t = mapper[head]
            else:
                t = RandomListNode(head.label)
                mapper[head] = t
            if phead is None:
                phead = t
                ptail = phead
            # handle next and random
            ptail.next = None
            if head.next is not None:
                if head.next in mapper:
                    t = mapper[head.next]
                else:
                    t = RandomListNode(head.next.label)
                ptail.next = t
            ptail.random = None
            if head.random is not None:
                if head.random in mapper:
                    t = mapper[head.random]
                else:
                    t = RandomListNode(head.random.label)
                ptail.random = t

            ptail = ptail.next
            head = head.next

        
        return phead

a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
a.next = b
b.next = c
a.random = c
c.random = b

obj = Solution()
res = obj.copyRandomList(a)
print res.label, res.next.label, res.random.label
