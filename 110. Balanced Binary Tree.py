# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalancedByDFS(self, root):
        return self.subDFS(root) != -1

    def subDFS(self, root):
        if root is None:
            return 0

        ld = self.subDFS(root.left)
        if ld == -1:
            return -1
        lr = self.subDFS(root.right)
        if lr == -1:
            return -1

        if abs(ld - lr) > 1:
            return -1

        return max(ld, lr) + 1

obj = Solution()
h = TreeNode(1)
print obj.isBalanced(h)