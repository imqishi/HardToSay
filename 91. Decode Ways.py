class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        res = [0] * (n + 1)
        res[n] = 1
        res[n-1] = 1 if s[n-1] != '0' else 0
        i = n - 2
        while i >= 0:
            if s[i] == '0':
                i -= 1
                continue
            t = int(s[i:i+2])
            res[i] = res[i+1] + res[i+2] if t >= 1 and t <= 26 else res[i+1]
            i -= 1
        
        return res[0]

    def numDecodingsFail(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.nums = 0
        s = s.lstrip('0')
        if len(s) == 0:
            return 0
        if s[-1] == '0':
            s = s.rstrip('0')
            s += '0'
        self.subNum(s)
        return self.nums
    
    def subNum(self, s):
        if s == '':
            self.nums += 1
            return

        if len(s) > 3 and s[2] == '0':
            self.subNum(s[1:])
            self.subNum(s[2:])
        elif len(s) > 2 and s[2] == '0':
            self.subNum(s[1:])
        elif len(s) > 1 and s[1] == '0':
            self.subNum(s[2:])
        else:
            self.subNum(s[1:])
            if len(s) >= 2 and int(s[:2]) < 27:
                self.subNum(s[2:])

obj = Solution()
print obj.numDecodings('12')