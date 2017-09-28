# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.fail = False
        self.check(root, [], None)
        return not self.fail

    def check(self, root, parents, type):
        if root is None:
            return

        if self.fail:
            return

        if type is not None:
            for i in parents:
                if type == 'left' and root.val >= i or type == 'right' and root.val <= i:
                    self.fail = True
                    return

        if root.left is not None:
            if root.val <= root.left.val:
                self.fail = True
                return

        if root.right is not None:
            if root.val >= root.right.val:
                self.fail = True
                return

        parents.append(root.val)
        self.check(root.left, parents, 'left')
        self.check(root.right, parents, 'right')
        parents.pop()