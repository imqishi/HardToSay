import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == -sys.maxint-1 and divisor == -1):
            return sys.maxint

        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            sign = 1
        else:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            child, i = divisor, 1
            while dividend >= child:
                dividend -= child
                result += i
                child = child << 1
                i = i << 1

        return result * sign

obj = Solution()
print obj.divide(10,2)
