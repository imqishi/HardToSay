# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.sum = 0
        self.traverse(root, str(root.val))
        return self.sum

    def traverse(self, root, subSum):
        if root.left is None and root.right is None:
            self.sum += int(subSum)
            return

        if root.left is not None:
            self.traverse(root.left, subSum + str(root.left.val))
        if root.right is not None:
            self.traverse(root.right, subSum + str(root.right.val))

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
obj = Solution()
print obj.sumNumbers(a)