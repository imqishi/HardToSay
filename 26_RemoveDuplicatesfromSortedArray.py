class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) == 0:
            return [nums, 0]
        while i < len(nums):
            if i == 0:
                i += 1
                continue
            if nums[i] == nums[i-1]:
                nums = nums[:i-1] + nums[i:]
            else:
                i += 1
        return [nums, len(nums)]
        # or directly return list(set(nums))


obj = Solution()
print obj.removeDuplicates([1])