class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = x
        while y * y > x:
            y = (x / y + y) / 2 
        
        return y

obj = Solution()
print obj.mySqrt(5)