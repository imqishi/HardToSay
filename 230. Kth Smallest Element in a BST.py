# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ret = None
        self.k = k
        self.traverse(root)
        return self.ret
    
    def traverse(self, root):
        if root.left is not None:
            self.traverse(root.left)
        
        self.k -= 1
        if self.k == 0:
            self.ret = root.val
            return
        if root.right is not None:
            self.traverse(root.right)
    
    def kthSmallestByBinary(self, root, k):
        count = self.countTree(root.left)
        if count <= k:
            return self.kthSmallestByBinary(root.left, k)
        elif k > count + 1:
            return self.kthSmallestByBinary(root.right, k - count - 1)

        return root.val
    
    def countTree(self, root):
        if root is None:
            return 0

        return 1 + self.countTree(root.left) + self.countTree(root.right)

a = TreeNode(2)
obj = Solution()
print obj.kthSmallest(a, 1)