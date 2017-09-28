# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        res.append([root])
        subres = [root]
        while len(subres) != 0:
            tmp = []
            for i in xrange(len(subres)):
                if subres[i].left is not None:
                    tmp.append(subres[i].left)
                if subres[i].right is not None:
                    tmp.append(subres[i].right)
            subres = tmp[:]
            if len(tmp) > 0:
                res.append(tmp[:])
        
        for i in xrange(len(res)):
            for j in xrange(len(res[i])):
                res[i][j] = res[i][j].val
        
        return res

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)
a1.left = a2
a2.right = a3
a1.right = a4
a4.left = a5
a4.right = a6
a6.left = a7
obj = Solution()
print obj.levelOrder(a1)