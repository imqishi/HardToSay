class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aLen = len(a)
        bLen = len(b)
        a = a[::-1]
        b = b[::-1]
        i = 0
        res = ''
        remainder = 0
        while i < aLen and i < bLen:
            t = int(a[i]) + int(b[i]) + remainder
            res += str(t % 2)
            remainder = t / 2
            i += 1

        if aLen > bLen:
            max = aLen
            maxNum = a
        else:
            max = bLen
            maxNum = b

        while i < max:
            t = int(maxNum[i]) + remainder
            res += str(t % 2)
            remainder = t / 2
            i += 1
        if remainder == 1:
            res += '1'

        return res[::-1]

obj = Solution()
print obj.addBinary('111', '11')
