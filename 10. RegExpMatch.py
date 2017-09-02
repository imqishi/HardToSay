class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0

        if p[1] == '*':
            return (self.isMatch(s, p[2:]) or len(s) != 0 and (s[0] == p[0] or '.' == p[0]) and self.isMatch(s[1:], p));
        else:
            return len(s) != 0 and (s[0] == p[0] or '.' == p[0]) and self.isMatch(s[1:], p[1:])

    def isMatchByDP(self, s, p):
        m = len(s)
        n = len(p)
        f = [[False for i in range(n + 1)] for i in range(m + 1)]
        f[0][0] = True
        i = 1
        while i <= m:
            f[i][0] = False
            i += 1

        j = 1
        while j <= n:
            f[0][j] = j > 1 and '*' == p[j-1] and f[0][j-2]
            j += 1

        i = 1
        while i <= m:
            j = 1
            while j <= n:
                if p[j-1] != '*':
                    f[i][j] = f[i-1][j-1] and (s[i-1] == p[j-1] or '.' == p[j-1])
                else:
                    f[i][j] = f[i][j-2] or ((s[i-1] == p[j-2] or '.' == p[j-2]) and f[i-1][j])
                j += 1
            i += 1

        return f[m][n]

obj = Solution()
print obj.isMatch('abc', 'ab.*')
print obj.isMatchByDP('abc', 'ab.*')
