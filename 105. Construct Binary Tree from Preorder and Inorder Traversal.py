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
        return self.subBuild(0, 0, len(inorder)-1)
    
    def subBuild(self, preStart, inStart, inEnd):
        if preStart > len(self.preorder) - 1 or inStart > inEnd:
            return None
            
        node = TreeNode(self.preorder[preStart])
        index = self.inorder.index(self.preorder[preStart])
        node.left = self.subBuild(preStart+1, inStart, index-1)
        node.right = self.subBuild(preStart+index-inStart+1, index+1, inEnd)
        return node

    def buildTreeLooply(self, preorder, inorder):
        stack_tree = []
        stack_val = []
        i = j = 0
        flag = False
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        root = node
        stack_tree.append(node)
        stack_val.append(preorder[0])
        i += 1

        while i < len(preorder):
            if len(stack_tree) > 0 and inorder[j] == stack_tree[-1].val:
                flag = True
                node = stack_tree[-1]
                stack_tree.pop()
                stack_val.pop()
                j += 1
            else:
                if flag is False:
                    stack_val.append(preorder[i])
                    node.left = TreeNode(preorder[i])
                    node = node.left
                    stack_tree.append(node)
                else:
                    flag = False
                    stack_val.append(preorder[i])
                    node.right = TreeNode(preorder[i])
                    node = node.right
                    stack_tree.append(node)
                
                i += 1
        
        return root

obj = Solution()
obj.buildTreeLooply([1,2], [2,1])