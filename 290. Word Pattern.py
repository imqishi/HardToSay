class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # format input
        mapper = {}
        strList = str.split(" ")
        newStr = ''
        alpha = 'a'
        for s in strList:
            if s not in mapper:
                mapper[s] = alpha
                newStr += alpha
                alpha = chr(ord(alpha) + 1)
            else:
                newStr += mapper[s]
        # format pattern
        mapper = {}
        newPattern = ''
        alpha = 'a'
        for ch in pattern:
            if ch not in mapper:
                mapper[ch] = alpha
                newPattern += alpha
                alpha = chr(ord(alpha) + 1)
            else:
                newPattern += mapper[ch]
        
        return newStr == newPattern
    

obj = Solution()
print obj.wordPattern('baab', 'dog cat cat dog')