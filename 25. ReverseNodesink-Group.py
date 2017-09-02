# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        nodeDict = {};
        for i in range(k):
            nodeDict[i] = []

        cur = head
        i = 0
        while cur:
            nodeDict[i % k].append(cur)
            i += 1
            cur = cur.next


        firstLen = len(nodeDict[0])
        lastLen = len(nodeDict[k-1])

        h = last = None
        for i in range(lastLen):
            for j in range(k)[::-1]:
                if h == None:
                    h = nodeDict[j][i]
                    last = h
                else:
                    last.next = nodeDict[j][i]
                    last = nodeDict[j][i]

        if firstLen != lastLen:
            for i in range(k):
                if firstLen == len(nodeDict[i]):
                    if h is not None:
                        last.next = nodeDict[i][firstLen-1]
                        last = nodeDict[i][firstLen-1]
                    else:
                        h = last = nodeDict[i][firstLen-1]
        last.next = None
        return h

    def reverseKGroupByRecursion(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroupByRecursion(cur, k)
            while count > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur

        return head




obj = Solution()
a = ListNode(1)
b = ListNode(2)
#c = ListNode(3)
#d = ListNode(4)
#e = ListNode(5)
a.next = b
#b.next = c
#c.next = d
#d.next = e
#a = None
rtn = obj.reverseKGroupByRecursion(a, 3)
while rtn:
    print rtn.val
    rtn = rtn.next
