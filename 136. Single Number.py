class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = 0
        for item in nums:
            target ^= item
        
        return target

obj = Solution()
print obj.singleNumber([1])