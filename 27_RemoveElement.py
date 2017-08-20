class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                if i == 0:
                    nums = nums[i+1:]
                else:
                    if len(nums) > i + 1:
                        nums = nums[:i] + nums[i+1:]
                    else:
                        nums = nums[:i]
            else:
                i += 1

        return nums

obj = Solution()
print obj.removeElement([3,2,2,3],3)
