class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

    def lengthOfLISNLogN(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ends = [0] * n
        Max = 0
        for x in nums:
            i, j = 0, Max
            while i != j:
                m = (i + j) / 2
                if ends[m] < x:
                    i = m + 1
                else:
                    j = m
            ends[i] = x
            Max = max(i + 1, Max)

        return Max

obj = Solution()
#print obj.lengthOfLIS([1,2,3,5])
#print obj.lengthOfLIS([1])
#print obj.lengthOfLIS([2,1])
#print obj.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print obj.lengthOfLIS([1,3,6,7,9,4,10,5,6])