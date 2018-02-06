# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        while self.between(root.val, p.val, q.val) is False:
            if root.val > p.val:
                root = root.left
            else:
                root = root.right
        
        return root

    def between(self, val, p, q):
        if (val >= p and val <= q) or (val >= q and val <= p):
            return True
        else:
            return False

a = TreeNode(1)
b = TreeNode(2)
a.right = b
obj = Solution()
print obj.lowestCommonAncestor(a, 1, 2).val