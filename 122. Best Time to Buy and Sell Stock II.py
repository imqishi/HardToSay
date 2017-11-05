class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        res = [0] * length
        for i in range(1, length):
            if prices[i] > prices[i-1]:
                res[i] = res[i-1] + prices[i] - prices[i-1]
            else:
                res[i] = res[i-1]
        
        return res[length-1]

obj = Solution()
print obj.maxProfit([7, 1, 5, 3, 6, 4])