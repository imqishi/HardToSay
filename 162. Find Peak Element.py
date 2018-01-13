class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 0

        for (i, num) in enumerate(nums):
            if i == 0:
                if num > nums[i+1]:
                    return 0
                continue
            elif i == len(nums) - 1:
                if num > nums[i-1]:
                    return i
            else:
                if num > nums[i-1] and num > nums[i+1]:
                    return i

obj = Solution()
print obj.findPeakElement([1,2,3,4,5,6])
print obj.findPeakElement([2,1])
print obj.findPeakElement([4,3,2,1])