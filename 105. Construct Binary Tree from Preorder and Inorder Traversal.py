# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        
    
    # inorder's left and right
    def subBuild(self, val, left, right):
        index = self.preorder.index(val)
        node = TreeNode(val)
        # find left's mid
        for i in len(left):
            if left[i] == self.preorder[index+1]:
                nl = left[:i]
                nr = left[i:]
        
        # find right's mid
        for i in len(right):
            if right[i] == :
                nl = right[:]