class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return False
        if numerator == 0:
            return '0'

        op = True if numerator * denominator > 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)
        # determine left part
        left = numerator / denominator
        rem = numerator % denominator

        if rem == 0:
            if op is False:
                return '-' + str(left)
            else:
                return str(left)

        # determine right part
        right = ''
        # record value and position
        everWalked = {}
        everWalked[rem] = 0
        while True:
            # append 0
            rem *= 10
            right += str(rem / denominator)
            rem %= denominator

            if rem in everWalked:
                right = right[:everWalked[rem]] + '(' + right[everWalked[rem]:] + ')'
                break
            else:
                everWalked[rem] = len(right)
            
            if rem == 0:
                break
        
        if op is False:
            ret = '-' + str(left) + '.' + str(right)
        else:
            ret = str(left) + '.' + str(right)
        return ret

obj = Solution()
print obj.fractionToDecimal(-50, 8)