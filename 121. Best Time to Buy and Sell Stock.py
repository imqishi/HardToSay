class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        min = prices[0]
        maxDiff = 0
        for i in range(1, length):
            diff = prices[i] - min
            if diff > maxDiff:
                maxDiff = diff
            if prices[i] < min:
                min = prices[i]

        return maxDiff

obj = Solution()
print obj.maxProfit([7,1,5,3,6,4])
print obj.maxProfit([7,6,4,3,1])