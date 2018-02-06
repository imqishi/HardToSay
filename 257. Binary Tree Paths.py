# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.res = []
        self.traverse(root, [])
        return self.res
    
    def traverse(self, root, subres):
        if root.left is None and root.right is None:
            self.res.append('->'.join(subres + [str(root.val)]))
            return

        if root.left is not None:
            self.traverse(root.left, subres + [str(root.val)])
        if root.right is not None:
            self.traverse(root.right, subres + [str(root.val)])

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
b.right = c
a.right = d
obj = Solution()
print obj.binaryTreePaths(a)