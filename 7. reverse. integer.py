class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tx = str(x)
        max = pow(2, 31) - 1
        min = - max - 1
        if x > max or x < min:
            return 0
        if tx[0] == '-':
            y = -int(tx[::-1][0:-1])
        else:
            y = int(tx[::-1])
        if y > max or y < min:
            return 0

        return y

obj = Solution()
print obj.reverse(1534236469)
