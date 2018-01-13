class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = []
        for num in nums:
            dp.append(num)
        
        for i in range(2, n):
            base = dp[i]
            t = 0
            for j in range(i - 1):
                if t is 0:
                    t = base + dp[j]
                else:
                    t = t if t > base + dp[j] else base + dp[j]
            dp[i] = t
        
        return max(dp)

obj = Solution()
print obj.rob([1,2,3,4,5,6])
print obj.rob([])
print obj.rob([1])
print obj.rob([1,2])
print obj.rob([2,1])
print obj.rob([1,3,1])