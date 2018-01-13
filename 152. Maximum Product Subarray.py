class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        ret = imin = imax = nums[0]
        for i in nums[1:]:
            if i < 0:
                imax, imin = imin, imax
            
            imax = max(i, imax * i)
            imin = min(i, imin * i)

            ret = max(ret, imax)

        return ret


obj = Solution()
print obj.maxProduct([-3, 2, -4, 5, -3])