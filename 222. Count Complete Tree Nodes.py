# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lh = self.height(root)
        if lh < 0:
            return 0

        if self.height(root.right) == lh - 1:
            return (1 << lh) + self.countNodes(root.right)
        else:
            return (1 << (lh - 1)) + self.countNodes(root.left)
    
    def height(self, root):
        if root is None:
            return -1
        else:
            return 1 + self.height(root.left)

    def myCountNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ptr = root
        self.llevel = 0
        while ptr is not None:
            self.llevel += 1
            ptr = ptr.left

        self.canExit = False
        self.lost = 0
        self.traverse(root, 0)
        return 2 ** self.llevel - self.lost - 1
        
    def traverse(self, root, level):
        if self.canExit:
            return

        if root is None:
            if level == self.llevel:
                self.canExit = True
                return
            else:
                self.lost += 1
                return
        
        self.traverse(root.right, level + 1)
        self.traverse(root.left, level + 1)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
obj = Solution()
print obj.countNodes(a)