class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        rem = 0
        while n != 1:
            rem = n % 2
            if rem == 1:
                return False
            n //= 2

        
        if n == 1 and rem == 1:
            return False
        else:
            return True

obj = Solution()
print obj.isPowerOfTwo(6)
print obj.isPowerOfTwo(2)
print obj.isPowerOfTwo(0)
print obj.isPowerOfTwo(1)
print obj.isPowerOfTwo(5)
print obj.isPowerOfTwo(8)
print obj.isPowerOfTwo(14)
print obj.isPowerOfTwo(16)
print obj.isPowerOfTwo(64)