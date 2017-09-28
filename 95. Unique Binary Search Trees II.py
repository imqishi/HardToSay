# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTreesByDP(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result = []
        for i in xrange(0, n+1):
            result.append([])
        if n == 0:
            return result[0]

        result[0].append(None);
        for len in xrange(1, n+1):
            for j in xrange(len):
                for lnode in result[j]:
                    for rnode in result[len-j-1]:
                        node = TreeNode(j + 1)
                        node.left = lnode
                        node.right = self.generateRightTree(rnode, j + 1)
                        result[len].append(node)

        return result[n]

    def generateRightTree(self, node, offset):
        if node is None:
            return None
        new_node = TreeNode(node.val + offset)
        new_node.left = self.generateRightTree(node.left, offset)
        new_node.right = self.generateRightTree(node.right, offset)
        return new_node 


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.subGenerate(1, n)
        
    
    def subGenerate(self, start, end):
        cur_list = []
        if start > end:
            cur_list.append(None)
            return cur_list
        
        if start == end:
            cur_list.append(TreeNode(start))
            return cur_list

        left = right = None
        i = start
        while i <= end:
            left = self.subGenerate(start, i-1)
            right = self.subGenerate(i+1, end)

            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    cur_list.append(root)
            i += 1
        
        return cur_list
