class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))

        for i in range(2, n):
            m = max(nums[i] + dp[i - 2], dp[i - 1])
            dp.append(m)
        
        return dp[-1]

obj = Solution()
print obj.rob([1,2,3,4,5,6])
print obj.rob([])
print obj.rob([1])
print obj.rob([1,2])
print obj.rob([2,1])
print obj.rob([1,3,1])