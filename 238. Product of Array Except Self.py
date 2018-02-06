class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nl = len(nums)
        res = [1] * (nl + 1)
        for i in range(1, nl + 1):
            res[i] = res[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(nl - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res[:-1]

obj = Solution()
print obj.productExceptSelf([1,2,3,4])