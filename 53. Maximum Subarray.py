import sys
import copy
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = len(nums)
        if maxLen == 0:
            return 0
        i = 1
        result = [0] * maxLen
        result[0] = maxVal = nums[0]
        while i < maxLen:
            if result[i-1] > 0:
                result[i] = nums[i] + result[i-1]
            else:
                result[i] = nums[i]
            if maxVal < result[i]:
                maxVal = result[i]
            i += 1

        return maxVal

    def maxSubArrayN2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = len(nums)
        if maxLen == 0:
            return 0
        i = 1
        result = copy.copy(nums)
        maxVal = max(nums)
        while i < maxLen:
            j = 0
            while j < maxLen:
                if i + j >= maxLen:
                    break
                result[j] = result[j] + nums[j+i]
                if maxVal < result[j]:
                    maxVal = result[j]
                j += 1
            i += 1

        return maxVal

obj = Solution()
print obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])