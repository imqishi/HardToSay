# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.subBuild(head, None)
        
    
    def subBuild(self, head, tail):
        fast = head
        slow = head
        if head == tail:
            return None

        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        
        node = TreeNode(slow.val)
        node.left = self.subBuild(head, slow)
        node.right = self.subBuild(slow.next, tail)
        return node