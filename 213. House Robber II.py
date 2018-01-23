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
        return max(self.robber(nums, 0, n - 2), self.robber(nums, 1, n - 1))
    
    def robber(self, nums, start, end):
        pre = cur = 0;
        for i in range(start, end + 1):
            temp = max(pre + nums[i], cur)
            pre = cur
            cur = temp
        return cur

obj = Solution()
print obj.rob([2, 1])