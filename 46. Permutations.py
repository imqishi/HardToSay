import copy
class Solution(object):
    result = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.sub_permute(nums, 0)
        return self.result
    
    def sub_permute(self, nums, start):
        if len(nums) == start + 1:
            self.result.append(copy.copy(nums))
            return

        size = len(nums)
        i = start
        while i < size:
            nums[start], nums[i] = nums[i], nums[start]
            self.sub_permute(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
            i += 1

obj = Solution()
print obj.permute([4,5,6])