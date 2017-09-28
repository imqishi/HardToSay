# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        while len(stack) > 0:
            tmp = []
            max = len(stack)
            for i in xrange(max):
                if i >= max / 2:
                    if stack[i] is not None:
                        tmp.append(stack[i].left)
                        tmp.append(stack[i].right)
                else:
                    if stack[i] is None:
                        # check if symmetric pos val same
                        if stack[max - i - 1] is not None:
                            return False
                    else:
                        # check if symmetric pos val same
                        if stack[max - i - 1] is None:
                            return False
                        if stack[max - i - 1].val != stack[i].val:
                            return False

                        tmp.append(stack[i].left)
                        tmp.append(stack[i].right)

            stack = tmp[:]
        return True

    def isSymmetricRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.subSym(root.left, root.right)
    
    def subSym(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False

        return self.subSym(left.left, right.right) and self.subSym(left.right, right.left)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(2)
a5 = TreeNode(3)
a1.left = a2
a1.right = a4
a2.right = a3
a4.right = a5
obj = Solution()
print obj.isSymmetric(a1)