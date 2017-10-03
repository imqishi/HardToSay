# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        return self.subBuildTree(len(postorder) - 1, 0, len(inorder) - 1)

    def subBuildTree(self, postorder_i, inorder_left, inorder_right):
        if postorder_i < 0 or inorder_left > inorder_right:
            return None

        node = TreeNode(self.postorder[postorder_i])
        middle_pos = self.inorder.index(self.postorder[postorder_i])
        node.left = self.subBuildTree(postorder_i - (inorder_right - middle_pos) - 1, inorder_left, middle_pos - 1)
        node.right = self.subBuildTree(postorder_i - 1, middle_pos + 1, inorder_right)
        return node

    def buildTreeLooply(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        
        stn = []
        root = TreeNode(postorder[-1])
        stn.append(root)
        postorder.pop()
        
        while True:
            if inorder[-1] == stn[-1].val:
                p = stn[-1]
                stn.pop()
                inorder.pop()
                if len(inorder) == 0:
                    break
                if len(stn) != 0 and inorder[-1] == stn[-1].val:
                    continue
                p.left = TreeNode(postorder[-1]) 
                postorder.pop()
                stn.append(p.left)
            else:
                p = TreeNode(postorder[-1])
                postorder.pop()
                stn[-1].right = p
                stn.append(p)

        return root

    def traverse(self, root):
        if root is None:
            return

        print root.val
        self.traverse(root.left)
        self.traverse(root.right)

obj = Solution()
#r = obj.buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1])
r = obj.buildTreeLooply([3,2,1], [3,2,1])
obj.traverse(r)