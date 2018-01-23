class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s = self.transform(s)
        t = self.transform(t)
        return s == t
    
    def transform(self, s):
        mapper = {}
        newCh = 'a'
        t = ''
        for ch in s:
            if ch not in mapper:
                mapper[ch] = newCh
                t += newCh
                newCh = chr(ord(newCh) + 1)
            else:
                t += mapper[ch]
        return t


obj = Solution()
print obj.isIsomorphic('', '')