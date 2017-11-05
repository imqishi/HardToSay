# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
    
    def flattenByLoop(self, root):
        if root is None:
            return None

        now = root
        while now is not None:
            if now.left is not None:
                pre = now.left
                while pre.right is not None:
                    pre = pre.right
                
                pre.right = now.right
                now.right = now.left
                now.left = None
            
            now = now.right

obj = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = d
d.left = e
d.right = f
b.left = c
obj.flatten(a)