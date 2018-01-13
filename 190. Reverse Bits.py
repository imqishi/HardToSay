class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)
        b_pos = b.find('b')
        b = b[b_pos+1:]
        b = b.rjust(32, '0')
        b = b[::-1]
        ret = 0
        for (i, num) in enumerate(b):
            ret += int(num) * pow(2, 32 - i - 1)
        
        return ret

    def reverseBitsBinaryOp(self, n):
        ret = 0;
        for i in range(32):
            ret += n & 1;
            n >>= 1;
            if i < 31:
                ret <<= 1;
        return ret

obj = Solution()
print obj.reverseBits(43261596)
print obj.reverseBitsBinaryOp(43261596)