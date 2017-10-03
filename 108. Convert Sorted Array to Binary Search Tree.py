# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None

        self.nums = nums
        return self.subBuild(length / 2, 0, length - 1)

    def subBuild(self, m_pos, left_pos, right_pos):
        if left_pos > right_pos or m_pos < left_pos or m_pos > right_pos:
            return None
        node = TreeNode(self.nums[m_pos])
        node.left = self.subBuild(left_pos + (m_pos - left_pos) / 2, left_pos, m_pos - 1)
        node.right = self.subBuild(m_pos + (right_pos - m_pos) / 2 + 1, m_pos + 1, right_pos)
        return node

    def traverse(self, root):
        if root is None:
            return
        print root.val
        self.traverse(root.left)
        self.traverse(root.right)

obj = Solution()
r = obj.sortedArrayToBST([1,2,3,4,5])
obj.traverse(r)