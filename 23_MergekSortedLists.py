# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        print len(lists[0])
        if len(lists) == 0:
            return None
        min = None
        pos = None
        head = None
        for index, node in enumerate(lists):
            if head is None:
                pos = index
                min = node.val
                head = node
            elif node.val < min:
                pos = index
                min = node.val
                head = node

        last = head
        lists[pos] = lists[pos].next

        while self.hasRemainedNode(lists):
            pos = self.findMin(lists)
            last.next = lists[pos]
            last = lists[pos]
            lists[pos] = lists[pos].next

        return head

    def hasRemainedNode(self, lists):
        for node in lists:
            if node is not None:
                return True

        return False

    def findMin(self, lists):
        pos = None
        min = None
        for index, node in enumerate(lists):
            if min is None:
                min = node.val
                pos = index
            elif node.val < min:
                min = node.val
                pos = index

        return pos

obj = Solution()
obj.mergeKLists([[]])